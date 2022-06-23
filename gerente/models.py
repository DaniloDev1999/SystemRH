from django.db import models

# Create your models here.
class gerente(models.Model):
    comissao = models.IntegerField()

    def __str__ (self):
        return self.comissao