from django.db import models

# Create your models here.
# models é uma classe python que representa uma tabela no banco de dados

class Usuario(models.Model):
    #campos do banco de dados
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255)
    idade = models.IntegerField()
    