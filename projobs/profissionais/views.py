# -*- coding: utf-8 -*-

from django.shortcuts import render
from django.views.generic import FormView

from .forms import ProfissionalForm


class CadastroView(FormView):
    form_class = ProfissionalForm
    template_name = 'profissionais/cadastro.html'
