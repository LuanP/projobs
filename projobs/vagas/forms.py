# -*- coding: utf-8 -*-

from django import forms

from .models import Vaga, Inscricao


class VagaForm(forms.ModelForm):
    class Meta:
        model = Vaga
        exclude = ('empresa', )


class InscricaoForm(forms.ModelForm):
    class Meta:
        model = Inscricao
        fields = ('pretensao_salarial', 'requisitos')
