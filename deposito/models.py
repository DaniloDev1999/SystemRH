from django.db import models

# Create your models here.
class deposito(models.Model):
    idDeposito = models.CharField(max_length=255)

    def __str__ (self):
        return self.idDeposito