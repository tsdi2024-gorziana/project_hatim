from datetime import datetime
from django.utils import timezone
from django.db import models
from modules_studets.models import Filers_modules
from filers.models import Filieres
from acountes.models import CustomUser


# Create your models here.
def user_directory_path(instance, filename):
    return f'files/{instance.user.username}/files/{filename}'

class Fiche_descptive(models.Model):
    title = models.CharField(max_length=100)
    type = models.CharField(max_length=100)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    file = models.FileField(upload_to=user_directory_path, null=True, blank=True)
    module = models.ForeignKey(Filers_modules, on_delete=models.CASCADE, null=True, blank=True)
    filer = models.ForeignKey(Filieres, on_delete=models.CASCADE ,null=True, blank=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.title}-{self.type}"

