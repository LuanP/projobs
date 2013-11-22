from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    area = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    logradouro = models.CharField(max_length=200)
