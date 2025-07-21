from django.contrib.auth.models import AbstractUser
from django.db import models


def user_directory_path(instance, filename):
    return f'users/{instance.username}/{filename}'

class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('formateur', 'Formateur'),
        ('administration', 'Administration'),
        ('admin', 'Admin'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=11, unique=True, null=True, blank=True)
    role = models.CharField(max_length=20, choices=ROLE_CHOICES)

    imge = models.FileField(upload_to=user_directory_path, null=True, blank=True,default='media/users/defult_prophile.png')

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def is_formateur(self):
        return self.role == 'formateur'

    def is_administration(self):
        return self.role == 'administration'

    def is_admin_custom(self):
        return self.role == 'admin' or self.is_superuser

    def __str__(self):
        return self.full_name