from django.contrib import admin

from .models import Vaga, ProcessoSeletivo, Inscricao, Entrevista


class VagaAdmin(admin.ModelAdmin):
    pass


class InscricaoInline(admin.TabularInline):
    model = Inscricao
    extra = 1


class ProcessoSeletivoAdmin(admin.ModelAdmin):
    inlines = [InscricaoInline, ]


class InscricaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vaga, VagaAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
admin.site.register(ProcessoSeletivo, ProcessoSeletivoAdmin)
