from django.contrib import admin
from apps.mascota.models import Vacuna, Mascota, Persona
# Register your models here.

admin.site.register(Vacuna)
admin.site.register(Mascota)
# admin.site.register(Raza)
admin.site.register(Persona)
