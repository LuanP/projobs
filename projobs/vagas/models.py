from django.db import models


class Vaga(models.Model):
    empresa = models.ForeignKey('empresas.Empresa')

    cargo = models.CharField(max_length=200)
    descricao = models.TextField()
    setor = models.CharField(max_length=200)
    inicio = models.DateField(blank=True, null=True)
    # requisitos = models.ForeignKey('Requisito', blank=True, null=True)


class ProcessoSeletivo(models.Model):
    vaga = models.ForeignKey('Vaga')
    profissionais = models.ManyToManyField(
        'profissionais.Profissional',
        through='Inscricao'
    )


class Inscricao(models.Model):
    data = models.DateField(auto_now_add=True)
    pretensao_salarial = models.CharField(max_length=200)
    nota_escrita = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_dinamica = models.PositiveSmallIntegerField(blank=True, null=True)
    nota_curriculo = models.PositiveSmallIntegerField(blank=True, null=True)


class Entrevista(models.Model):
    inscricao = models.ForeignKey('Inscricao')

    relatorio = models.TextField()
