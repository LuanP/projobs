from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView

from empresas.views import EmpresaBaseMixin
from profissionais.views import ProfissionalBaseMixin
from .forms import VagaForm, InscricaoForm
from .models import Vaga, Inscricao


class CadastroView(EmpresaBaseMixin, CreateView):
    model = Vaga
    template_name = 'vagas/cadastro.html'
    form_class = VagaForm
    success_url = reverse_lazy('empresas:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.empresa_id = self.get_object().pk
        self.object.save()
        form.save_m2m()
        messages.success(self.request, 'Vaga cadastrada com sucesso!')
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
        messages.success(self.request, 'Vaga atualizada com sucesso!')
        return HttpResponseRedirect(self.get_success_url())

    def get_object(self, queryset=None):
        obj = super(AtualizarView, self).get_object(queryset)
        self.empresa_id = obj.pk
        return obj.vaga_set.get(pk=self.kwargs.get('pk'))


class InscricaoView(ProfissionalBaseMixin, CreateView):
    model = Inscricao
    form_class = InscricaoForm
    success_url = reverse_lazy('profissionais:home')

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.processo_seletivo_id = self.kwargs.get('pk')
        self.object.profissional_id = self.request.user.pk
        self.object.save()
        form.save_m2m()
        messages.success(self.request, 'Inscrição realizada. Boa sorte!')
        return HttpResponseRedirect(self.get_success_url())
