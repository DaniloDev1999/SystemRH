from django.db import models

# Create your models here.
class boleto(models.Model):
    nomeCliente = models.CharField(max_length=255)
    codigoCliente = models.CharField(max_length=255)

    def __str__ (self):
        return self.nomeCliente