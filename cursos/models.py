from time import clock_settime
from django.db import models

# Create your models here.
class Nota(models.Model):
    # disciplina = ForeignKey
    
    nota_disciplina = models.FloatField(default=0.0, blank=False, null=False)

    def __str__(self):
        return f"Nota: Disciplina: {self.nota_disciplina}"

class Curso(models.Model):

    nome_curso = models.CharField(max_length=150)

    #disciplinas(lista) = ForeignKey

    qtd_vagas = models.IntegerField(default=0, null=False, blank=False)
    
    def __str__(self) -> str:
        return f"Curso: {self.nome_curso}"

'''
class Frequencia():

    Criar objeto modelo

    lista = []
    def add(self, novo):
        self.lista.append(novo)
'''

    

