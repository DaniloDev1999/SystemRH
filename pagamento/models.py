from django.db import models
from django.forms import DateField

# Create your models here.
class pagamento(models.Model):
    pagamento = models.IntegerField()
    formaPagamento = models.CharField(max_length=255)
    parcelaPagamento = models.IntegerField()
    dataPagamento = DateField()
    bancoPag = models.CharField(max_length=255)
    agenciaPag = models.CharField(max_length=255)
    contaPag = models.CharField(max_length=255)
    
    def __str__ (self):
        return self.formaPagamento