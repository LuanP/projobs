# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import CreateView, TemplateView

from .forms import EmpresaForm


class EmpresaHomeView(TemplateView):
    template_name = 'empresas/home.html'


class CadastroView(CreateView):
    form_class = EmpresaForm
    template_name = 'empresas/cadastro.html'
    success_url = '/'
