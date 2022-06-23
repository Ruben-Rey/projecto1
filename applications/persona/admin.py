from django.contrib import admin

from applications.persona.models import Persona
from applications.persona.models import Habilidades


class EmpleadoAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'departamento',
        'job',
    )

admin.site.register(Persona, EmpleadoAdmin)
