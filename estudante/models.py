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
        ('S', 'Solteiro(a)'), 
        ('C', 'Casado(a)'), 
        ('V', 'Viúvo(a)'),
        ('H', 'Separado(a)'),
        ('D', 'Divorciado(a)'),
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
    password = models.CharField(max_length=160, blank=False)

    def __str__(self):
        return f'Discente {self.nome}'
    
class Matricula(models.Model):
    '''id_matricula = models.OneToOneField(Alunos, on_delete=models.PROTECTED)
    curso = models.ForeignKey(Cursos, blank = False)
    '''
    data_matricula = models.DateTimeField()
    usuario_responsavel = models.CharField(max_length = 100, blank = False, unique = False)

    def __str__(self) -> str:
       return f"Matricula do(a) {self.nome}"

class Pais(models.Model):
    #pais_id = models.ForeignKey(Alunos, on_delete=models.CASCADE, blank = False, null=True)
    nome_pai = models.CharField(max_length = 100, blank = False, unique = False)
    nome_mae = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    password = models.CharField(max_length = 160, blank = False) #Verificar: Documentação Django para Password

    def __str__(self) -> str:
        return f"Pai {self.nome_pai}, Mae {self.nome_mae}"

class Egresso(models.Model):
    cpf = CPFField('cpf')#.ForeignKey(Aluno, blank = False, unique = True)
    nome_egresso = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    password = models.CharField(max_length = 160, blank = False) #Verificar: Documentação Django para Password
    #curso = models.ForeignKey(Cursos, blank = False)
    
    def __str__(self) -> str:
        return f"Nome do Egresso {self.nome_egresso}"


