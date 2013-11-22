# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url

from .views import CadastroView, EmpresaHomeView


urlpatterns = patterns('',
    url(r'^$', EmpresaHomeView.as_view(), name='home'),
    url(r'^cadastro/$', CadastroView.as_view(), name='cadastro'),
)
