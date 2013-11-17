from django.contrib import admin

from .models import Profissional, FormacaoProfissional, FormacaoAcademica


class FormacaoAcademicaInline(admin.TabularInline):
    model = FormacaoAcademica


class FormacaoProfissionalInline(admin.TabularInline):
    model = FormacaoProfissional


class ProfissionalAdmin(admin.ModelAdmin):
    inlines = [
        FormacaoProfissionalInline,
        FormacaoAcademicaInline,
    ]


admin.site.register(Profissional, ProfissionalAdmin)
