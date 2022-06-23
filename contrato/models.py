from django.db import models

# Create your models here.
class contrato(models.Model):
    dadosCorretor = models.CharField(max_length=255)
    dadosCliente = models.CharField(max_length=255)
    descricaoImovel = models.CharField(max_length=255)
    valor = models.IntegerField()
    documentacao = models.CharField(max_length=255)
    clausulaPenal = models.CharField(max_length=255)

    def __str__ (self):
        return self.dadosCorretor