from django.contrib.auth.models import User, Group
from django.db import models
# -*- coding: utf-8 -*-
from django.db import models

class Aluno (models.Model):
    nomeUsuario = models.ForeignKey (User)
    matricula = models.IntegerField()

    def __str__(self):
        return 'Usuário: {0} - Matrícula: {1}'.format(self.nomeUsuario, self.matricula)

class Atendente (models.Model):
    grupo = models.ForeignKey(Group)
    nomeUsuario = models.ForeignKey(User)

class TipoDocumento (models.Model):
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return self.descricao

class Documentos (models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento)
    preco = models.FloatField(max_length=6)
    tempo = models.TimeField()
    descricao = models.CharField(max_length=2000)

class StatusDocumento (models.Model):
    status = models.CharField(max_length=25)

    def __str__(self):
        return self.status

class Servico (models.Model):
    documento = models.ForeignKey(Documentos)
    aluno = models.ForeignKey(Aluno)
    status = models.ForeignKey(StatusDocumento)


