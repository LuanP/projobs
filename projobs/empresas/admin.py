from django.contrib import admin

from .models import Empresa


class EmpresaAdmin(admin.ModelAdmin):
    pass


admin.site.register(Empresa, EmpresaAdmin)
