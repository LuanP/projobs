# -*- coding: utf-8 -*-

from django.db import models

from core.models import BaseCadastro


class Empresa(BaseCadastro):
    nome = models.CharField(max_length=200)
