from django.db import models

# Create your models here.

class Via(models.Model):
    nome_via = models.CharField(max_length=20)

    def __str__(self):
        return self.nome_via

class Medicamento(models.Model):
    titulo = models.CharField(max_length=20)
    nome = models.CharField(max_length=150)
    posologia = models.CharField(max_length=150)
    quantidade = models.CharField(max_length=150, default="_______ 01 CAIXA")
    via = models.ForeignKey(Via, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo

