from django.db import models


class Empresa(models.Model):
    nome = models.CharField(max_length=200)
    email = models.EmailField()
    cidade = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
