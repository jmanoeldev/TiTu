from django.db import models
from django.contrib.auth.models import User

class Experimento(models.Model):
    """
    Representa um conjunto de réplicas de uma mesma análise,
    ex: "Amostra Vinagre A". Define o método volumétrico usado.
    """

    TIPO_ACIDO_BASE = 'acido_base'
    TIPO_REDOX = 'redox'
    TIPO_COMPLEXOMETRICA ='complexometrica'
    TIPO_PRECIPITACAO = 'precipitacao'

    TIPO_CHOICES = [
        (TIPO_ACIDO_BASE, 'Ácido-base'),
        (TIPO_REDOX, 'Redox'),
        (TIPO_COMPLEXOMETRICA, 'Complexometrica'),
        (TIPO_PRECIPITACAO, 'Precipitação'),
    ]

    # Referência ao usuário dono do experimento
    usuario = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name = 'experimentos'
    )
    # Nome de identificação do experimento
    nome = models.CharField(max_length = 100)

    # Tipo de titulação (método volumétrico), restrito às opções de TIPO_CHOICES.
    tipo = models.CharField(max_length = 20, choices = TIPO_CHOICES)
    data_realizacao = models.DateField()
    criado_em = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome