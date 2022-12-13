from email.policy import default
from django.db import models
from cpf_field.models import CPFField
from django.contrib.auth.hashers import make_password, check_password
from django.contrib.auth.models import User

from endereco.models import Endereco
from cursos.models import Curso


# Create your models here.
class Employee(models.Model):
    sexo_choices = (
        ('H', 'Homem Cis'), 
        ('M', 'Mulher Cis'),
        ('K', 'Homem Trans'),
        ('W', 'Mulher Trans')
    )
    estado_civil_choices = (
        ('S', 'Solteiro(a)'), 
        ('C', 'Casado(a)'), 
        ('V', 'Viúvo(a)'),
        ('H', 'Separado(a)'),
        ('D', 'Divorciado(a)'),
        ('U', 'União Estável')
    )
    
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nome = models.CharField(max_length=130, blank=False, unique=True)
    email = models.EmailField(max_length=130, blank=False)
    password = models.CharField(max_length=160, blank=False)

    telefone = models.CharField(max_length=16, blank=False)
    
    ''' CPF -> xxx.xxx.xxx-xx or xxxxxxxxxxx '''
    #cpf = models.CharField(max_length=14, blank=False, unique=True)
    cpf = CPFField('cpf')

    ''' RG -> xxxxxxxxxxxxx '''
    rg = models.CharField(max_length=13, blank=True, unique=True)
    
    data_nascimento = models.DateField(max_length=8, blank=True, null=True)
    sexo = models.CharField(max_length=1, choices=sexo_choices, blank=True)
    estado_civil = models.CharField(max_length=1, choices=estado_civil_choices, blank=True)
    naturalidade = models.CharField(max_length=30, blank=True)
    
    endereco = models.ForeignKey(Endereco, on_delete=models.DO_NOTHING, null=True, blank=True, unique=False)

    def __str__(self) -> str:
        return self.nome()

    def set_password(self, password):
        self.password = make_password(password)
    
    def check_password_user(self, password):
        return check_password(password, self.password)

    class Meta:
        abstract = True

class Gestor(Employee):
    def __str__(self) -> str:
        return f'Gestor {self.nome}'
    
    class Meta:
        permissions = (("views_gestor", "pode ver views do grupo gestor"),)


class Coordenador(Employee):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True, blank=True)
    

    def __str__(self) -> str:
        return f'Coordenador {self.nome}'
    
    class Meta:
        permissions = (("views_coordenador", "pode ver views do grupo coordenador"),)
    

class Professor(Employee):
    curso = models.ForeignKey(Curso, on_delete=models.DO_NOTHING, null=True, blank=True, unique=False)
    
    #disciplinas = models.ManyToManyField(Cursos)

    carga_horaria = models.IntegerField(null=True, blank=True)
    
    def __str__(self) -> str:
        return f'Professor {self.nome}'
    
    class Meta:
        permissions = (("views_professor", "pode ver views do grupo professor"),)
    