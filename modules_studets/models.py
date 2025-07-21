from django.db import models
from filers.models import Filieres
from acountes.models import CustomUser

class Filers_modules(models.Model):
    titer_module = models.CharField("Titre du module", max_length=255, unique=True)
    referance_uf = models.CharField("Référence UF", max_length=25, unique=True)
    titer_module_pransipale = models.CharField("Titre principal", max_length=255, blank=True, null=True)
    filere = models.ManyToManyField(Filieres, related_name='filers_modules', verbose_name="Filières")
    nbr_sequence = models.PositiveIntegerField("Nombre de séquences", default=0)
    heraire_totale = models.PositiveIntegerField("Heures totales", default=0)

    def __str__(self):
        return f"{self.titer_module} ({self.referance_uf})"



class Seaquesnces_modules(models.Model):
    titer_sequence = models.CharField("Titre de la séquence", max_length=255, unique=True)
    objectif_sequence = models.CharField("Objectif", max_length=255, blank=True, null=True)
    total_hores = models.PositiveIntegerField("Total des heures", default=0)
    order = models.PositiveIntegerField("Order", default=0)
    module = models.ForeignKey(Filers_modules, on_delete=models.CASCADE, related_name='sequences', verbose_name="Module")

    def __str__(self):
        return f"{self.titer_sequence} ({self.total_hores}h)"



class Chapitres_sequenses(models.Model):
    titre = models.CharField("Titre", max_length=255)
    description = models.TextField("Description")
    order = models.PositiveIntegerField("Ordre", default=0)
    duree = models.PositiveIntegerField("Durée (min)", default=0)
    sequenses = models.ForeignKey(Seaquesnces_modules, on_delete=models.CASCADE, related_name='chapitres', verbose_name="Séquence")

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f"{self.order}. {self.titre}"



class Affectation(models.Model):
    formateur = models.ForeignKey(CustomUser, on_delete=models.CASCADE, verbose_name="Formateur")
    filiere = models.ForeignKey(Filieres, on_delete=models.CASCADE, verbose_name="Filière")
    modules = models.ManyToManyField(Filers_modules, related_name='affectations', verbose_name="Modules affectés")

    class Meta:
        unique_together = ('formateur', 'filiere')
        verbose_name = "Affectation"
        verbose_name_plural = "Affectations"

    def __str__(self):
        return f"{self.formateur} - {self.filiere}"


class AffectationSequence(models.Model):
    affectation = models.ForeignKey('Affectation', on_delete=models.CASCADE, related_name='sequences')
    sequence = models.ForeignKey('Seaquesnces_modules', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('affectation', 'sequence')
        verbose_name = "Affectation Séquence"
        verbose_name_plural = "Affectations Séquences"

    def __str__(self):
        return f"{self.affectation.formateur} - {self.sequence.titer_sequence}"


class AffectationChapitre(models.Model):
    affectation_sequence = models.ForeignKey('AffectationSequence', on_delete=models.CASCADE, related_name='chapitres')
    chapitre = models.ForeignKey('Chapitres_sequenses', on_delete=models.CASCADE)

    class Meta:
        unique_together = ('affectation_sequence', 'chapitre')
        verbose_name = "Affectation Chapitre"
        verbose_name_plural = "Affectations Chapitres"

    def clean(self):
        # Check that the chapitre belongs to the selected sequence
        if self.chapitre.sequenses != self.affectation_sequence.sequence:
            raise ValidationError("This chapitre does not belong to the selected sequence.")

    def __str__(self):
        return f"{self.affectation_sequence} - {self.chapitre.titre}"
