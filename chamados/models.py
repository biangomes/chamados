from tkinter import CASCADE
from django.db import models

# Create your models here.
# TODO: criar model de Usuario

class Chamado(models.Model):
    sccd = models.BigIntegerField(default=0000)
    titulo = models.TextField()
    descricao = models.TextField(blank=True, null=True)
    cliente = models.CharField(max_length=100)
    dtAbertura = models.DateTimeField(auto_now=True)
    dtVencimento = models.DateTimeField(auto_now=True)
    dtEncaminhamento = models.DateTimeField(auto_now=True)
    severidade = models.PositiveIntegerField(default=5)


# TODO: o analista pode ser um proprio model User
# class Analista(models.Model):
#     nome = models.CharField(max_length=100)
    

class Modulo(models.Model):
    nome = models.CharField(max_length=255)


class Cliente(models.Model):
    nome = models.CharField(max_length=100)


class Modulo_Cliente(models.Model):
    cliente_pk = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    modulo_pk = models.ForeignKey(Modulo, on_delete=models.CASCADE)


class Analise(models.Model):
    # TODO: implementar usuario/analista
    # usuario_id = models.ForeignKey(nalista, on_delete=models.CASCADE)
    chamado_pk = models.ForeignKey(Chamado, on_delete=models.CASCADE)