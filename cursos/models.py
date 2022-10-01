#from time import clock_settime
from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator, MaxValueValidator
"""from django.shortcuts import render
from django.http import HttpResponseRedirect
from somewhere import handle_uploaded_file
from django import forms"""

#Min and Max values
class MinMaxFloat(models.FloatField):
    def __init__(self, min_value=None, max_value=None, *args, **kwargs):
        self.min_value, self.max_value = min_value, max_value
        super(MinMaxFloat, self).__init__(*args, **kwargs)

    def formfield(self, **kwargs):
        defaults = {'min_value': self.min_value, 'max_value' : self.max_value}
        defaults.update(kwargs)
        return super(MinMaxFloat, self).formfield(**defaults)

# Create your models here.
class Nota(models.Model):
    # disciplina = ForeignKey

    nota_disciplina = MinMaxFloat(min_value=0.0, max_value=10.0)

    def __str__(self):
        return f"Nota: Disciplina: {self.nota_disciplina}"


class Curso(models.Model):

    nome_curso = models.CharField(max_length=150)

    # disciplinas(lista) = ForeignKey

    quantidade_vagas = models.PositiveIntegerField(default=0, null=False, blank=False)


    def __str__(self) -> str:
        return f"Curso: {self.nome_curso}"


class Disciplina(models.Model):
    """id_disciplina = chave primaria"""

    nome_disciplina = models.CharField(max_length=150)

    """alunos = chave estrangeira"""

    """curso = chave estrangeira"""

    """professor = chave estrangeira"""

    """semestre = chave estrangeira"""

    quantidade_vagas = models.PositiveIntegerField(default=0, null=False, blank=True)

    quantidade_creditos = models.PositiveIntegerField(
        default=0, null=False, blank=True)

    tipo_disciplina_choices = (
        ('OB', 'Obrigatória'),
        ('OP', 'Optativa'),
    )

    tipo_disciplina = models.CharField(max_length=150, choices=tipo_disciplina_choices, blank=True)

    # dia_aula = data formato dia

    # hora_aula = data formato hh:mm

    carga_horaria = models.CharField(max_length=150)

    conteudo_ministrado = models.CharField(
        max_length=255, null=False, blank=True)

    # material_disciplina = upload de arquivos

    def __str__(self) -> str:
        return f"Disciplina: {self.nome_disciplina}"


#Upload de arquivos 
"""class UploadFileForm(forms.Form):
    title = forms.CharField(max_length=255)
    file = forms.FileField()

    def handle_uploaded_file(f):
        with open('some/file/name.txt', 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

    def upload_file(request):
        if request.method == 'POST':
            form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
                handle_uploaded_file(request.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadFileForm()
        return render(request, 'upload.html', {'form': form})
"""

class Frequencia(models.Model):
     
    """id_disciplina = models.ForeignKey(
         get_user_model(),
         max_length = 14,
         primary_key = True,
         on_delete = models.CASCADE
         #related_name = "matricula",
    )"""

    data_aula = models.DateField()

    titulo_dias_aula = models.CharField(max_length = 255, default=True)

    DATE_FIELD = ['lista_dias_aula']
    REQUIRED_FIELDS = ['titulo_dias_aula'] 

    def __str__(self) -> str:
       return f"Frequencia de {self.titulo_dias_aula}"
