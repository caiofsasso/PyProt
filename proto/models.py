from django.contrib.auth.models import User, Group
from django.db import models
# -*- coding: utf-8 -*-
from django.db import models

class Aluno (models.Model):
    nomeUsuario = models.ForeignKey(User, related_name='Nome Usuário', verbose_name='Nome Usuário')
    matricula = models.IntegerField(verbose_name='Matrícula')

    def __str__(self):
        return 'Usuário: {0} - Matrícula: {1}'.format(self.nomeUsuario, self.matricula)

    class Meta:
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

class Atendente (models.Model):
    grupo = models.ForeignKey(Group, related_name='Grupo')
    nomeUsuario = models.ForeignKey(User, verbose_name='Nome Usuário', related_name='Nome Usuario')

    class Meta:
        verbose_name = 'Atendente'
        verbose_name_plural = 'Atendentes'

class TipoDocumento (models.Model):
    descricao = models.CharField(max_length=100, verbose_name='Descrição')

    def __str__(self):
        return self.descricao

    class Meta:
        verbose_name = 'Tipo de Documento'
        verbose_name_plural = 'Tipos de Documento'

class Documentos (models.Model):
    tipoDocumento = models.ForeignKey(TipoDocumento, verbose_name='Tipo Documento', related_name='Tipo Documento')
    preco = models.FloatField(max_length=6, verbose_name='Preço')
    tempo = models.TimeField(verbose_name='Tempo')
    descricao = models.CharField(max_length=2000, verbose_name='Descrição')

    class Meta:
        verbose_name = 'Documento'
        verbose_name_plural = 'Documentos'

class StatusDocumento (models.Model):
    status = models.CharField(max_length=25, verbose_name='Status')

    def __str__(self):
        return self.status

    class Meta:
        verbose_name = 'Status Documento'
        verbose_name_plural = 'Status Documentos'

class Servico (models.Model):
    documento = models.ForeignKey(Documentos, related_name='Documento', verbose_name='Documento')
    aluno = models.ForeignKey(Aluno, related_name='Aluno', verbose_name='Aluno')
    status = models.ForeignKey(StatusDocumento, related_name='Status', verbose_name='Status')

    class Meta:
        verbose_name = 'Serviço'
        verbose_name_plural = 'Serviços'


