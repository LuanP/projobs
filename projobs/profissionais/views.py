# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import CreateView

from .forms import ProfissionalForm


class CadastroView(CreateView):
    form_class = ProfissionalForm
    template_name = 'profissionais/cadastro.html'
    success_url = '/'
