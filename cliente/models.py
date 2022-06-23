from django.db import models

# Create your models here.
class cliente (models.Model):
    dataCadastro=models.DateField()
    
    def consultar_imovel(self):
        print("A consulta foi cadastrada para o dia", self.dataCadastro)

    def manter_Conta(self):
        print("A conta foi mantida com sucesso")

    def agendar_visita(self):
        print("A visita foi agendada com sucesso")
        
    def _str__ (self):
        return self.dataCadastro