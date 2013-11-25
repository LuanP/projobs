# -*- coding: utf-8 -*-

from django import forms

from accounts.forms import AccountForm
from .models import Empresa


class EmpresaForm(AccountForm):
    class Meta:
        model = Empresa
        fields = (
            'username', 'password1', 'password2', 'email', 'company_name',
            'area', 'estado', 'cidade', 'logradouro'
        )
