from django.db import models

# Create your models here.
class transferencia(models.Model):
    tipo = models.CharField(max_length=255)
    codIdentificacao = models.CharField(max_length=255)

    def __str__ (self):
        return self.cartorio