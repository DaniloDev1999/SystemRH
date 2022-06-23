from django.db import models

# Create your models here.
class agendamento(models.Model):
    dia = models.DateField()
    hora = models.DateField()
    local = models.CharField(max_length=255)

    def __str__ (self):
        return self.local