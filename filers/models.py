from django.db import models
from acountes.models import CustomUser
# Create your models here.
class AcademicYear(models.Model):
    name = models.CharField(max_length=100)
    annee = models.CharField(max_length=25)

    def __str__(self):
        return self.name

class Filieres(models.Model):
    title = models.CharField(max_length=100, unique=False)
    academic_year = models.ForeignKey(AcademicYear, on_delete=models.PROTECT)
    formateurs = models.ManyToManyField(CustomUser, related_name='filieres')

    def __str__(self):
        return f"{self.title} ({self.academic_year}) "





