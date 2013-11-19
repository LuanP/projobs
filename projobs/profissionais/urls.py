# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from .views import CadastroView


urlpatterns = patterns('',
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastro'),
)
