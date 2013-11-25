# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from django.contrib.auth.decorators import login_required

from .views import CadastroView, ProfissionalHomeView


urlpatterns = patterns('',
    url(r'^$', login_required(ProfissionalHomeView.as_view()), name='home'),
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastro'),
)
