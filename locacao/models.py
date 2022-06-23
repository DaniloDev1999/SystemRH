from django.db import models

# Create your models here.
class locacao(models.Model):
    dataDesocupacao = models.DateField()
    periodo = models.DateField()
    formaGarantia = models.CharField(max_length=255)
    fiador = models.CharField(max_length=255)

    def __str__ (self):
        return self.formaGarantia