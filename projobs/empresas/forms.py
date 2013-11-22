# -*- coding: utf-8 -*-

from django import forms

from .models import Empresa


class EmpresaForm(forms.ModelForm):
    class Meta:
        model = Empresa
        fields = (
            'username', 'email', 'password', 'company_name', 'area', 'estado',
            'cidade', 'logradouro'
        )
