import string
from django.db import models

# Create your models here.
class pessoa(models.Model):
    matricula= models.IntegerField()
    telefone = models.CharField(max_length=11)
    cep =models.CharField(max_length=9)
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=20)
    cidade = models.CharField(max_length=20)
    uf = models.CharField(max_length=3)

    def __str__ (self):
        return self.telefone
        