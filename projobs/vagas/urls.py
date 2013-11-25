# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import CadastroView


urlpatterns = patterns('',
    url(
        r'^cadastro/$',
        login_required(CadastroView.as_view()),
        name='cadastro'
    ),
)
