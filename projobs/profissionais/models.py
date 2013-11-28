# -*- coding: utf-8 -*-

from django.db import models

from accounts.models import User


class Profissional(User):
    rg = models.CharField(max_length=200, blank=True, null=True)
    cpf = models.CharField(max_length=200, blank=True, null=True)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=200, blank=True, null=True)

    class Meta:
        verbose_name_plural = u'Profissionais'

    def __unicode__(self):
        return self.get_full_name()


class FormacaoProfissional(models.Model):
    profissional = models.ForeignKey('Profissional')

    empresa = models.CharField(max_length=200)
    cargo = models.CharField(max_length=200)
    inicio = models.DateField()
    termino = models.DateField(blank=True, null=True)
    atual = models.BooleanField()

    class Meta:
        verbose_name_plural = u'Formações Profissionais'

    def __unicode__(self):
        return u'{} ({} em {})'.format(self.profissional, self.cargo,
                                       self.empresa)

    # to do on forms
    # def clean_termino(self, *args, **kwargs):
    #     if self.cleaned_data['termino'] < self.cleaned_data['inicio']:
    #         raise forms.ValidationError("""
    #             A data de término não pode ser depois da data de início.
    #         """)


class FormacaoAcademica(models.Model):
    profissional = models.ForeignKey('Profissional')

    curso = models.CharField(max_length=200)
    instituicao = models.CharField(max_length=200)
    data_conclusao = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name_plural = u'Formações Acadêmicas'

    def __unicode__(self):
        return u'{} ({} em {})'.format(self.profissional, self.curso,
                                       self.instituicao)
