from django.db import models
from datetime import datetime

TIPO_SANGUE = (
		('ap', 'A+'),
		('an', 'A-'),
		('bp', 'B+'),
		('bn', 'B-'),
		('abp', 'AB+'),
		('abn', 'AB-'),
		('op', 'O+'),
		('on', 'O-'),
	)

class Endereco(models.Model):
	logradouro = models.CharField(max_length = 50, verbose_name = 'logradouro')
	numero = models.IntegerField()
	estado = models.CharField(max_length = 20, verbose_name = 'estado')
	cidade = models.CharField(max_length = 20, verbose_name = 'cidade')

class Hospital(models.Model):
	nome = models.CharField(max_length = 30, verbose_name = 'nome')
	telefone = models.CharField(max_length = 14, verbose_name = 'telefone')
	endereco = models.OneToOneField('Endereco', on_delete = models.CASCADE, related_name = 'hospital_endereco')


class Hemocentro(models.Model):
	nome = models.CharField(max_length = 30, verbose_name = 'nome')
	telefone = models.CharField(max_length = 14, verbose_name = 'telefone')
	estoque_sanguineo = models.ForeignKey('Estoque', on_delete = models.CASCADE, related_name = 'meu_Estoque')
	endereco = models.OneToOneField('Endereco', on_delete = models.CASCADE, related_name = 'hemocentro_endereco')

class Doador(models.Model):
	SEXO = (
		('F', 'Feminino'),
		('M', 'Masculino'),
	)

	nome = models.CharField(max_length = 30, verbose_name = 'nome')
	cpf = models.CharField(max_length = 11, verbose_name = 'cpf')
	sexo = models.CharField(max_length = 1, choices = SEXO)
	telefone = models.CharField(max_length = 14, verbose_name = 'telefone')
	dt_nascimento = models.DateField(auto_now = False)
	endereco = models.ForeignKey('Endereco', on_delete = models.CASCADE, related_name = 'doador_endereco')
	tipo_sangue = models.CharField(max_length = 3, choices = TIPO_SANGUE)

class Estoque(models.Model):
	tipo_sangue = models.CharField(max_length = 3, choices = TIPO_SANGUE)
	quant_bolsas = models.IntegerField()


class Doacao(models.Model):
	doador = models.ForeignKey('Doador', on_delete = models.CASCADE, related_name = 'doacoes_realizadas') 
	hemocentro = models.ForeignKey('Hemocentro', on_delete = models.CASCADE, related_name = 'doacoes_recebidas')
	data_doacao =  models.DateField(auto_now = True)
	quant_bolsas = models.IntegerField()
	direcionada = models.BooleanField()
	paciente = models.CharField(max_length = 30, verbose_name = 'paciente')
	hospital = models.ForeignKey('Hospital', on_delete = models.CASCADE, related_name = 'doacoes_direcionadas')


class Transacao(models.Model):
	tipo_sangue = models.CharField(max_length = 3, choices = TIPO_SANGUE)
	emissor = models.ForeignKey('Hemocentro', on_delete = models.CASCADE, related_name = 'repasses')
	receptor = models.ForeignKey('Hospital', on_delete = models.CASCADE, related_name = 'recebidos')
	data_transacao = models.DateField(auto_now = True)
	quant_bolsas = models.IntegerField()


		