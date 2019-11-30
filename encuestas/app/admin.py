from django.contrib import admin

# Register your models here.

from app.models import Pregunta, Respuesta

admin.site.register(Pregunta)
admin.site.register(Respuesta)