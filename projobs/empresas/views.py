# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import EmpresaForm
from .models import Empresa


class EmpresaHomeView(DetailView):
    model = Empresa
    template_name = 'empresas/home.html'

    def dispatch(self, *args, **kwargs):
        try:
            obj = self.get_object()
        except Empresa.DoesNotExist:
            return redirect('{}?next={}'.format(
                settings.LOGIN_URL,
                self.request.path
            ))
        return super(EmpresaHomeView, self).dispatch(*args, **kwargs)

    def get_object(self, queryset=None):
        return Empresa.objects.get(pk=self.request.user.pk)

class CadastroView(CreateView):
    form_class = EmpresaForm
    template_name = 'empresas/cadastro.html'
    success_url = '/'
