from django.db import models

# Create your models here.
class imovel(models.Model):
    matricula = models.IntegerField()
    valor_imo = models.IntegerField()
    rua = models.CharField(max_length=255)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    uf = models.CharField(max_length=255)
    tamanho = models.CharField(max_length=255)
    comodos = models.CharField(max_length=255)
    garagem = models.CharField(max_length=255)
    tipoImovel = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    cep = models.CharField(max_length=255)

    def __str__ (self):
        return self.rua