from django.contrib import admin
from .models import Gestor, Coordenador, Professor

# Register your models here.
admin.site.register(Gestor)
admin.site.register(Coordenador)
admin.site.register(Professor)