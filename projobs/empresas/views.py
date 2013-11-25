# -*- coding: utf-8 -*-

from django.conf import settings
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import EmpresaForm
from .models import Empresa


class EmpresaBaseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Empresa.DoesNotExist:
            return redirect('{}?next={}'.format(
                settings.LOGIN_URL,
                request.path
            ))
        return super(EmpresaBaseMixin, self).dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        return Empresa.objects.get(pk=self.request.user.pk)


class EmpresaHomeView(EmpresaBaseMixin, DetailView):
    model = Empresa
    template_name = 'empresas/home.html'


class CadastroView(CreateView):
    form_class = EmpresaForm
    template_name = 'empresas/cadastro.html'
    success_url = '/'
