from django.db import models
from cpf_field.models import CPFField

#from endereco.models import Endereco
#from cursos.models import Cursos


# Create your models here.
class Employee(models.Model):
    sexo_choices = (
        ('H', 'Homem Cis'), 
        ('M', 'Mulher Cis'),
        ('K', 'Homem Trans'),
        ('W', 'Mulher Trans')
    )
    estado_civil_choices = (
        ('S', 'Solteiro'), 
        ('C', 'Casado'), 
        ('V', 'Viúvo'),
        ('H', 'Separado'),
        ('D', 'Divorciado'),
        ('U', 'União Estável')
    )
    
    nome = models.CharField(max_length=130, blank=False)
    email = models.EmailField(max_length=130, blank=False)
    senha = models.CharField(max_length=60, blank=False)

    telefone = models.CharField(max_length=16, blank=False)
    
    ''' CPF -> xxx.xxx.xxx-xx or xxxxxxxxxxx '''
    #cpf = models.CharField(max_length=14, blank=False, unique=True)
    cpf = CPFField('cpf')

    ''' RG -> xxxxxxxxxxxxx '''
    rg = models.CharField(max_length=13, blank=True, unique=True)
    
    data_nascimento = models.DateField(max_length=8, blank=True)
    sexo = models.CharField(max_length=1, choices=sexo_choices, blank=True)
    estado_civil = models.CharField(max_length=1, choices=estado_civil_choices, blank=True)
    naturalidade = models.CharField(max_length=30, blank=True)
    
    '''
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
    '''

    def __str__(self) -> str:
        return self.nome()


class Gestor(Employee):
    def __str__(self) -> str:
        return f'Gestor {self.nome}'
    

class Coordenador(Employee):
    '''
    curso = models.ForeignKey(Cursos)
    '''

    def __str__(self) -> str:
        return f'Coordenador {self.nome}'
    

class Professor(Employee):
    '''
    cursos = models.ForeignKey(Cursos)
    disciplinas = models.ManyToManyField(Cursos)
    '''

    carga_horaria = models.IntegerField(null=True, blank=False)

    def __str__(self) -> str:
        return f'Professor {self.nome}'
    
'''
class list():
    lista = []

    def add(self, novo):
        self.lista.append(novo)
'''