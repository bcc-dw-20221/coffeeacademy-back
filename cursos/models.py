from time import clock_settime
from django.db import models
"""from django.shortcuts import render
from django.http import HttpResponseRedirect
from somewhere import handle_uploaded_file
from django import forms"""



# Create your models here.
class Nota(models.Model):
    # disciplina = ForeignKey

    nota_disciplina = models.FloatField(default=0.0, blank=False, null=False)

    def __str__(self):
        return f"Nota: Disciplina: {self.nota_disciplina}"


class Curso(models.Model):

    nome_curso = models.CharField(max_length=150)

    # disciplinas(lista) = ForeignKey

    quantidade_vagas = models.IntegerField(default=0, null=False, blank=False)

    def __str__(self) -> str:
        return f"Curso: {self.nome_curso}"


class Disciplina(models.Model):
    """id_disciplina = chave primaria"""

    nome_disciplina = models.CharField(max_length=150)

    """alunos = chave estrangeira"""

    """curso = chave estrangeira"""

    """professor = chave estrangeira"""

    """semestre = chave estrangeira"""

    quantidade_vagas = models.IntegerField(default=0, null=False, blank=True)

    quantidade_creditos = models.IntegerField(
        default=0, null=False, blank=True)

    tipo_disciplina_choices = (
        ('OB', 'Obrigatória'),
        ('OP', 'Optativa'),
    )

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