# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import CreateView

from .forms import EmpresaForm


class CadastroView(CreateView):
    form_class = EmpresaForm
    template_name = 'empresas/cadastro.html'
    success_url = '/'
