from django.contrib import admin

from .models import Profissional, FormacaoProfissional, FormacaoAcademica


class ProfissionalAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profissional, ProfissionalAdmin)
