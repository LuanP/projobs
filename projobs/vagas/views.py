from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from django.views.generic import CreateView

from empresas.views import EmpresaBaseMixin
from .forms import VagaForm
from .models import Vaga


class CadastroView(EmpresaBaseMixin, CreateView):
    model = Vaga
    template_name = 'vagas/cadastro.html'
    form_class = VagaForm
    success_url = reverse_lazy('empresas:home')

    def get_form_kwargs(self):
        kwargs = super(CadastroView, self).get_form_kwargs()
        if kwargs.get('data'):
            data = kwargs['data'].copy()
            data['empresa'] = self.user.pk
            kwargs['data'] = data
        return kwargs
