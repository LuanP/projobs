# -*- coding: utf-8 -*-

from django import forms

from .models import Profissional


class ProfissionalForm(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = (
            'first_name', 'last_name', 'username', 'email', 'password',
            'data_nascimento', 'telefone', 'rg', 'cpf', 'area', 'estado',
            'cidade', 'logradouro'
        )
