# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import FormView

from .forms import EmpresaForm


class CadastroView(FormView):
    form_class = EmpresaForm
    template_name = 'empresas/cadastro.html'
