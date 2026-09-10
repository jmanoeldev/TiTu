from django.db import models
from .experimento import Experimento
from .solucao_titulante import SolucaoTitulante

class Titulacao(models.Model):
    """
    Representa uma réplica individual de titulação, vinculada a um
    Experimento (o grupo de réplicas) e a uma SolucaoTitulante usada.
    """

    # A qual experimento (grupo de réplicas) essa titulação pertence.
    experimento = models.ForeignKey(
        Experimento, on_delete = models.PROTECT, related_name = 'titulacoes'
    )

    # Qual solução titulante foi usada nessa réplica específica.
    # on_delete=PROTECT: IMPEDE apagar uma solução titulante se ela já foi
    solucao_titulante = models.ForeignKey(
        SolucaoTitulante, on_delete = models.PROTECT, related_name = 'titulacoes'
    )

    # Volume gasto de titulante na bureta, em mL
    volume_titulante = models.DecimalField(max_digits = 8, decimal_places = 2)

    # Volume (ou massa) da amostra usado na titulação
    volume_amostra = models.DecimalField( max_digits = 8, decimal_places = 2)

    coeficiente_titulante = models.PositiveSmallIntegerField(default=1)
    coeficiente_analito = models.PositiveSmallIntegerField(default=1)

    # Resultado calculado
    # Fica nulo até o sistema calcular e salvar
    concentracao_calculada = models.DecimalField(
        max_digits = 10, decimal_places = 5, null = True, blank = True
    )

    criado_em = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return f'{self.experimento.nome} - réplica de {self.criado_em.date()}'