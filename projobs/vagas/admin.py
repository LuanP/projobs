from django.contrib import admin

from .models import Vaga, ProcessoSeletivo, Inscricao, Entrevista


class VagaAdmin(admin.ModelAdmin):
    pass


class ProcessoSeletivoAdmin(admin.ModelAdmin):
    pass


class InscricaoAdmin(admin.ModelAdmin):
    pass


admin.site.register(Vaga, VagaAdmin)
admin.site.register(ProcessoSeletivo, ProcessoSeletivoAdmin)
admin.site.register(Inscricao, InscricaoAdmin)
