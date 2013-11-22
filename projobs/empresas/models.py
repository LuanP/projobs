# -*- coding: utf-8 -*-

from django.db import models

from accounts.models import User


class Empresa(User):
    company_name = models.CharField(max_length=200)
