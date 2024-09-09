from django.db import models

# Create your models here.

class Usuario(models.Model):
    nome = models.CharField(max_length=100)
    cpf = models.CharField( primary_key=True, max_length=11)
    data = models.DateField()

    def __str__(self):
        return self.nome