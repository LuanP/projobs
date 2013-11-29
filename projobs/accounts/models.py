# -*- coding: utf-8 -*-

import uuid

from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.contrib.sites.models import Site
from django.db import models
from django.core.mail.message import EmailMessage
from django.template.loader import render_to_string


class User(AbstractUser):
    area = models.CharField(max_length=200, blank=True, null=True)
    estado = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=200, blank=True, null=True)
    logradouro = models.CharField(max_length=200)
    activation_key = models.CharField(
        max_length=200,
        default= lambda: unicode(uuid.uuid4()),
        unique=True,
    )

    def email_user(self, subject, message, from_email=None):
        email = EmailMessage(
            subject,
            message,
            from_email,
            [self.email, ],
        )
        email.send()

    def send_activation_email(self):
        context = {
            'activation_key': self.activation_key,
            'site': Site.objects.get_current(),
        }

        message = render_to_string(
            'accounts/activation_text.txt',
            context,
        )

        self.email_user(u'[Projobs] Ativação da conta', message)
