from django.core.urlresolvers import reverse_lazy
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from empresas.views import EmpresaBaseMixin
from .forms import VagaForm
from .models import Vaga


class CadastroView(EmpresaBaseMixin, CreateView):
    model = Vaga
    template_name = 'vagas/cadastro.html'
    form_class = VagaForm
    success_url = reverse_lazy('empresas:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.empresa_id = self.get_object().pk
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class VagaListView(ListView):
    model = Vaga
    context_object_name = 'vagas'


class AtualizarView(EmpresaBaseMixin, UpdateView):
    model = Vaga
    form_class = VagaForm
    success_url = reverse_lazy('empresas:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.empresa_id = self.empresa_id
        self.object.save()
        form.save_m2m()
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        obj = super(AtualizarView, self).get_object(queryset)
        self.empresa_id = obj.pk
        return obj.vaga_set.get(pk=self.kwargs.get('pk'))
