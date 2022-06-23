from django.db import models

# Create your models here.
class pessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=255)
    razaoSocial = models.CharField(max_length=255)
    representanteLegal = models.CharField(max_length=255)

    def __str__ (self):
        return self.cnpj