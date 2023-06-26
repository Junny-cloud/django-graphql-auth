from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    telephone = models.CharField(max_length=30, null=True, blank=True, verbose_name="Téléphone")
    fonction = models.CharField(max_length=200, null=True, blank=True, verbose_name="Fonction")
    entreprise = models.CharField(max_length=200, null=True, blank=True, verbose_name="Entreprise")
    photo_profile = models.ImageField(upload_to="photo", null=True, blank=True, verbose_name="Photo profile")
    email = models.EmailField(blank=False, max_length=254, verbose_name="email address")

    USERNAME_FIELD = "username"  # e.g: "username", "email"
    EMAIL_FIELD = "email"  # e.g: "email", "primary_email"
