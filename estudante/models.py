from django.db import models
from cpf_field.models import CPFField

from django.contrib.auth.models import User
from django.contrib.auth.hashers import make_password, check_password

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

    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    matricula = models.CharField(max_length=15, blank = False, unique = True, primary_key = True)
    nome = models.CharField(max_length = 255, blank=False, unique=True)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length = 1, choices=sexo_choices, blank=True)
    
    ''' CPF -> xxx.xxx.xxx-xx or xxxxxxxxxxx '''
    cpf = CPFField('cpf')

    ''' RG -> xxxxxxxxxxxxx '''
    rg = models.CharField(max_length = 15, blank=False, unique=True)

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
    
    def set_password(self, password):
        self.password = make_password(password)
    
    def check_password_user(self, password):
        return check_password(password, self.password)

    class Meta:
        permissions = (("views_alunos", "pode ver views do grupo aluno"),)
    
class Matricula(models.Model):
    id_matricula = models.OneToOneField(Alunos, on_delete=models.CASCADE, related_name="discente")

    '''
    curso = models.ForeignKey(Cursos, blank = False)
    '''
    data_matricula = models.DateTimeField()
    usuario_responsavel = models.CharField(max_length = 100, blank = False, unique = False)

    def __str__(self) -> str:
       return f"Matricula do(a) {self.id_matricula}"

class Pais(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    pais_id = models.ForeignKey(Alunos, on_delete=models.CASCADE, blank = False, null=True, related_name="pai")
    nome_pai = models.CharField(max_length = 100, blank = False, unique = False)
    nome_mae = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    password = models.CharField(max_length = 160, blank = False) #Verificar: Documentação Django para Password

    def __str__(self) -> str:
        return f"Pai {self.nome_pai}, Mae {self.nome_mae}"
    
    def set_password(self, password):
        self.password = make_password(password)
    
    def check_password_user(self, password):
        return check_password(password, self.password)

    class Meta:
        permissions = (("views_pais", "pode ver views do grupo pais"),)

class Egresso(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    id_matricula_egresso = models.OneToOneField(Alunos, on_delete=models.CASCADE, related_name="egressos")
    #cpf = CPFField('cpf')
    nome_egresso = models.CharField(max_length = 100, blank = False, unique = False)
    email = models.EmailField()
    password = models.CharField(max_length = 160, blank = False) #Verificar: Documentação Django para Password
    #curso = models.ForeignKey(Cursos, blank = False)
    
    def __str__(self) -> str:
        return f"Nome do Egresso {self.nome_egresso}"

    def set_password(self, password):
        self.password = make_password(password)
    
    def check_password_user(self, password):
        return check_password(password, self.password)
        
    class Meta:
        permissions = (("views_egresso", "pode ver views do grupo egresso"),)

