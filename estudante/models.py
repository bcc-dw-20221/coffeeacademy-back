from django.db import models
from django.contrib.auth import get_user_model
from cpf_field.models import CPFField

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
    
    matricula = models.ForeignKey(
         get_user_model(),
         max_length = 14,
         primary_key = True,
         on_delete = models.CASCADE
         #related_name = "matricula",
    )

    nome = models.CharField(max_length = 255, blank=False, unique=True)

    data_nascimento = models.DateField()

    sexo = models.CharField(max_length = 1, choices=sexo_choices, blank=True)

    cpf = CPFField('cpf')

    rg = models.CharField(max_length = 8, blank=False, unique=True)

    #endereco = models.ForeignKey(
        #get_user_model(),
        #on_delete=models.CASCADE,
        #related_name="endereco",
    #)

    telefone = models.CharField(max_length = 16)

    #disciplina = models.ForeignKey(
        #get_user_model(),
        #on_delete=models.CASCADE,
        #related_name="disciplina",
    #)

    #pais = models.ForeignKey(
    #    get_user_model(), 
    #    on_delete=models.CASCADE
    #   releted_name="pais"
    #)

    estado_civil = models.CharField(max_length = 1, choices=estado_civil_choices, blank=True)

    naturalidade = models.CharField(max_length = 20)

    email = models.EmailField(max_length=254)
    
    senha = models.CharField(max_length = 30)

    def __str__(self):
        return self,matricula



