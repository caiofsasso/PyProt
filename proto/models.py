from django.contrib.auth.models import User
from django.db import models
# -*- coding: utf-8 -*-
from django.db import models

class Aluno (models.Model):
    nomeUsuario = models.ForeignKey (User)
    matricula = models.IntegerField(max_length=300)

class Atendente (models.Model):
    nomeUsuario = models.CharField (User)

class TipoDocumento (models.Model):
    descricao = models.CharField(max_length=100)

class Documentos (models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento)
    preco = models.FloatField(max_length=6)
    tempo = models.TimeField()
    descricao = models.CharField(max_length=2000)

class StatusDocumento (models.Model):
    status = models.CharField(max_length=25)

class Servico (models.Model):
    documento = models.ForeignKey(Documentos)
    aluno = models.ForeignKey(Aluno.matricula)
    status = models.ForeignKey(StatusDocumento)


