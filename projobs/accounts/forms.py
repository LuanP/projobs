# -*- coding: utf-8 -*-

from django import forms

from .models import User


class AccountForm(forms.ModelForm):
    password1 = forms.CharField(label=u'Senha', widget=forms.PasswordInput)
    password2 = forms.CharField(
        label=u'Confirmação de senha',
        widget=forms.PasswordInput,
        help_text=u'Digite novamente, para verificação'
    )

    class Meta:
        model = User

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                'As senhas não conferem',
                code='password_mismatch',
            )
        return password2

    def save(self, commit=True):
        user = super(AccountForm, self).save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
