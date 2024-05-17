from django.db import models

# Create your models here.

class Solicitacao(models.Model):
    inicio_colaborador = models.DateField()
    nome = models.CharField(max_length=100)
    sobrenome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=255)
    email_corporativo = models.EmailField()
    gestor_direto = models.CharField(max_length=100)
    grupo_email = models.CharField(max_length=50)
    cargo = models.CharField(max_length=100)
    departamento = models.CharField(max_length=100)
    cliente = models.CharField(max_length=100)
    dispositivo_solicitado = models.CharField(max_length=50)
    codigo_ativo = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} {self.sobrenome} - {self.dispositivo_solicitado}'