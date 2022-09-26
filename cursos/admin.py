from django.contrib import admin
from cursos.models import Nota, Curso, Disciplina, Frequencia

# Register your models here.
admin.site.register(Nota)
admin.site.register(Curso)
admin.site.register(Disciplina)
admin.site.register(Frequencia)
