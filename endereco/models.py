from mailbox import NotEmptyError
from pyexpat import model
from django.db import models

class Endereco(models.Model):
    rua = models.CharField(max_length=150, null=False)
    numero = models.CharField(max_length=20, null=False)
    complemento = models.CharField(max_length=150)
    bairro = models.CharField(max_length=150)
    cidade = models.CharField(max_length=150)
    cep = models.CharField(max_length=9)
    '''cep = models.ForeignKey(Endereco,
    on_delete=models.CASCADE
    blank=False
    max_length=9
    )'''

    def __str__(self):
        return f'Rua {self.rua}, nº {self.numero}, complemento {self.complemento}, bairro {self.bairro}, cidade {self.cidade}, cep {self.cep}'


