from django.db import models

# Create your models here.
class pessoaFisica(models.Model):
    nome = models.CharField(max_length=255)
    cpf = models.CharField(max_length=255)
    rg = models.CharField(max_length=255)
    sexo = models.CharField(max_length=255)
    dataNascimento = models.DateField(max_length=255)

    def __str__ (self):
        return self.nome