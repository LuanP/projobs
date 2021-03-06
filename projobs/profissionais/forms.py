# -*- coding: utf-8 -*-

from django import forms

from accounts.forms import AccountForm
from .models import Profissional


class ProfissionalForm(AccountForm):
    data_nascimento = forms.DateField(
        widget=forms.TextInput(attrs={'id': 'datepicker'})
    )

    class Meta:
        model = Profissional
        fields = (
            'first_name', 'last_name', 'username', 'password1', 'password2',
            'email', 'data_nascimento', 'telefone', 'rg', 'cpf', 'area',
            'estado', 'cidade', 'logradouro'
        )
