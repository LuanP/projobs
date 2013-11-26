# -*- coding: utf-8 -*-

from django.db import models


class Vaga(models.Model):
    empresa = models.ForeignKey('empresas.Empresa')

    cargo = models.CharField(max_length=200)
    descricao = models.TextField()
    setor = models.CharField(max_length=200)
    inicio = models.DateField(blank=True, null=True)
    quantidade = models.PositiveSmallIntegerField(default=1)
    requisitos = models.ManyToManyField('Requisito', blank=True, null=True)

    def __unicode__(self):
        return u'{} em {}'.format(self.cargo, self.empresa.company_name)


class ProcessoSeletivo(models.Model):
    vaga = models.ForeignKey('Vaga')
    profissionais = models.ManyToManyField(
        'profissionais.Profissional',
        through='Inscricao'
    )
    ativo = models.BooleanField(default=True)


class Inscricao(models.Model):
    processo_seletivo = models.ForeignKey('ProcessoSeletivo')
    profissional = models.ForeignKey('profissionais.Profissional')

    data = models.DateField(auto_now_add=True)
    pretensao_salarial = models.CharField(max_length=200)
    nota_escrita = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_dinamica = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_curriculo = models.PositiveSmallIntegerField(blank=True, null=True)
    requisitos = models.ManyToManyField('Requisito')

    class Meta:
        verbose_name_plural = u'Inscrições'


class Entrevista(models.Model):
    inscricao = models.ForeignKey('Inscricao')

    relatorio = models.TextField()


class Requisito(models.Model):
    requisito = models.CharField(max_length=200)

    def __unicode__(self):
        return self.requisito
