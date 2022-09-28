from django.db import models
from cpf_field.models import CPFField

#from endereco.models import Endereco
#from cursos.models import Cursos
#from cursos.models import Disciplina

# Create your models here.
class Alunos(models.Model):
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

    matricula = models.CharField(max_length=15, blank = False, unique = True, primary_key = True)
    nome = models.CharField(max_length = 255, blank=False, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length = 1, choices=sexo_choices, blank=True)
    
    ''' CPF -> xxx.xxx.xxx-xx or xxxxxxxxxxx '''
    cpf = CPFField('cpf')

    ''' RG -> xxxxxxxxxxxxx '''
    rg = models.CharField(max_length = 8, blank=False, unique=True)

    '''
    endereco = models.OneToOneField(Endereco, on_delete=models.DO_NOTHING)
    '''
    telefone = models.CharField(max_length=16, blank=False)

    '''
    cursos = models.ForeignKey(Cursos)
    disciplinas = models.ManyToManyField(Cursos)
    pais = models.oneToOneField(Pais, on_delete=models.DO_NOTHING)
    '''

    estado_civil = models.CharField(max_length = 1, choices=estado_civil_choices, blank=True)
    naturalidade = models.CharField(max_length = 20)

    email = models.EmailField(max_length=130, blank=False)
    senha = models.CharField(max_length=60, blank=False)

    def __str__(self):
        return self.nome
    
class Matricula(models.Model):
    '''id_matricula = models.OneToOneField(Alunos, on_delete=models.PROTECTED)
    curso = models.ForeignKey(Cursos, blank = False)
    '''
    data_matricula = models.DateTimeField()
    usuario_responsavel = models.CharField(max_length = 100, blank = False, unique = False)

    def __str__(self) -> str:
       return f"Matricula do(a) {self.aluno.nome}"

class Pais(models.Model):
   #id_pais = models.ForeignKey(aluno, blank = False)
    nome_pai = models.CharField(max_length = 100, blank = False, unique = False)
    nome_mae = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    senha = models.CharField(max_length = 50, blank = False, unique = False) #Verificar: Documentação Django para Password

    def __str__(self) -> str:
        return f"Pais do(a) {self.aluno.nome}"

class Egresso(models.Model):
    cpf = CPFField('cpf')#.ForeignKey(Aluno, blank = False, unique = True)
    nome_egresso = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    senha = models.CharField(max_length = 50, blank = False, unique = False) #Verificar: Documentação Django para Password
    #curso = models.ForeignKey(Cursos, blank = False)
    
    def __str__(self) -> str:
        return f"Nome do Egresso {self.aluno.nome}"








