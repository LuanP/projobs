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

    def __unicode__(self):
        return u'{} - {}'.format(self.vaga.empresa, self.vaga.cargo)


class Inscricao(models.Model):
    SITUACAO_CHOICES = (
        (0, 'Em processo'),
        (1, 'Aprovado'),
        (2, 'Reprovado'),
    )
    processo_seletivo = models.ForeignKey('ProcessoSeletivo')
    profissional = models.ForeignKey('profissionais.Profissional')

    data = models.DateField(auto_now_add=True)
    pretensao_salarial = models.CharField(max_length=200)
    nota_escrita = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_dinamica = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_curriculo = models.PositiveSmallIntegerField(blank=True, null=True)
    requisitos = models.ManyToManyField('Requisito', blank=True, null=True)
    situacao = models.IntegerField(choices=SITUACAO_CHOICES, default=0)

    class Meta:
        verbose_name_plural = u'Inscrições'
        unique_together = ('profissional', 'processo_seletivo')

    def __unicode__(self):
        return u'{} em {}'.format(self.profissional, self.processo_seletivo)


class Entrevista(models.Model):
    inscricao = models.ForeignKey('Inscricao')

    relatorio = models.TextField()

    def __unicode__(self):
        return u'relatório de {}'.format(self.inscricao)


class Requisito(models.Model):
    requisito = models.CharField(max_length=200)

    def __unicode__(self):
        return self.requisito
