from django.contrib import admin
from estudante.models import Alunos, Matricula, Pais, Egresso

# Register your models here.
admin.site.register(Alunos)
admin.site.register(Matricula)
admin.site.register(Pais)
admin.site.register(Egresso)