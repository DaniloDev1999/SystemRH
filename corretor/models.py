from django.db import models

# Create your models here.
class corretor(models.Model):
    comissao = models.IntegerField()
    idCorretor = models.CharField(max_length=255)

    def __str__ (self):
        return self.idCorretor