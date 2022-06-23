from django.db import models

# Create your models here.
class Login(models.Model):
    email = models.CharField(max_length=255)
    senha = models.CharField(max_length=255)
    permissao = models.CharField(max_length=255)

    def __str__ (self):
        return self.email