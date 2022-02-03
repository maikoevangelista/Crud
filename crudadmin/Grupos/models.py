from django.db import models

# Create your models here.

class Grupos(models.Model):
    nome = models.CharField(max_length=100)
    Sobrenome = models.CharField(max_length=100)
    data_nascimento = models.DateField(blank=True, null=True)
    Naturalidade = models.CharField(max_length=100)
    hobby = models.CharField(max_length=100)

