from django.db import models
from django.contrib.auth.models import User # sistema de usuario pronto do Django

class SolucaoTitulante(models.Model):
    """
    Representa uma solução titulante já cadastrada pelo técnico,
    ex: 'NaOH 0,1 M - lote 3' pode ser reutilizada em outras titulações
    """

    # Referência ao usuario dono dessa solução
    # on_delete = cascade: se o usuario for apagado, as soluções são apagadas junto.
    # related_name: permite acessar via usuario.solucoes_titulantes.all()
    usuario = models.ForeignKey(
        User, on_delete = models.CASCADE, related_name= 'solucoes_titulantes'
    )

    # Nome de identificação da solução (texto curto, até 100 caracteres)
    nome = models.CharField(max_length = 100)

    # Concentração "teórica"
    concentracao_nominal = models.DecimalField(max_digits= 10, decimal_places = 5)

    # Fator de correção, calculado após a padronização (ex: 0,982).
    fator_correcao = models.DecimalField(
        max_digits = 6, decimal_places = 4, null = True, blank = True
    )

    # Data em que a padronização foi criada
    data_padronizacao = models.DateField(null = True, blank = True)

    #Data de criação do registro
    criado_em = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.nome

s1 = SolucaoTitulante()