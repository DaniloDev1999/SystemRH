from django.db import models

# Create your models here.
class aviso(models.Model):
    matricula = models.IntegerField()
    assunto = models.CharField(max_length=255)
    dataAviso = models.DateField()

    def __str__ (self):
        return self.assunto