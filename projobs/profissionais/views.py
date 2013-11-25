# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import ProfissionalForm
from .models import Profissional


class ProfissionalHomeView(DetailView):
    model = Profissional
    template_name = 'profissionais/home.html'

    def dispatch(self, *args, **kwargs):
        try:
            obj = self.get_object()
        except Profissional.DoesNotExist:
            return redirect('{}?next={}'.format(
                settings.LOGIN_URL,
                self.request.path
            ))
        return super(ProfissionalHomeView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return Profissional.objects.get(pk=self.request.user.pk)


class CadastroView(CreateView):
    form_class = ProfissionalForm
    template_name = 'profissionais/cadastro.html'
    success_url = '/'
