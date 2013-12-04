# -*- coding: utf-8 -*-

from django.conf import settings
from django.contrib import messages
from django.shortcuts import render, redirect
from django.views.generic import CreateView, DetailView

from .forms import ProfissionalForm
from .models import Profissional


class ProfissionalBaseMixin(object):
    def dispatch(self, request, *args, **kwargs):
        try:
            self.get_object()
        except Profissional.DoesNotExist:
            return redirect('{}?next={}'.format(
                settings.LOGIN_URL,
                request.path
            ))
        return super(ProfissionalBaseMixin, self).dispatch(
            request, *args, **kwargs
        )

    def get_object(self, queryset=None):
        return Profissional.objects.get(pk=self.request.user.pk)


class ProfissionalHomeView(ProfissionalBaseMixin, DetailView):
    model = Profissional
    template_name = 'profissionais/home.html'
    context_object_name = 'profissional'


class CadastroView(CreateView):
    form_class = ProfissionalForm
    template_name = 'profissionais/cadastro.html'
    success_url = '/'

    def form_valid(self, form):
        response = super(CadastroView, self).form_valid(form)
        self.object.send_activation_email()
        messages.success(
            self.request,
            "Foi enviada uma mensagem de ativação para seu e-mail. "
            "Favor verificar"
        )
        return response
