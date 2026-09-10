from abc import ABC, abstractmethod #serve de molde para outras classes, ambos os métodos vão herdar o método de calcular_concentracao
from decimal import Decimal

class CalculadoraTitulacao(ABC):
    """
    Classe base para o cálculo de concentração numa titulação.
    Cada subclasse implementa sua própria fórmula, mas todos recebem os mesmo
    3 dados de entrada
    """

    def __init__(self, volume_titulante, volume_amostra, concentracao_titulante,
                 coeficiente_titulante=1, coeeficiente_analito=1):
        #Decimal garante a precisao usada nos models e nao mistura float com decimal
        self.volume_titulante = Decimal(volume_titulante)
        self.volume_amostra = Decimal(volume_amostra)
        self.concentracao_titulante = Decimal(concentracao_titulante)
        self.coeficiente_titulante = Decimal(coeficiente_titulante)
        self.coeficiente_analito = Decimal(coeeficiente_analito)

    @abstractmethod
    def calcular_concentracao(self):
        mols_titulante = self.concentracao_titulante * self.volume_titulante

        fator = self.coeficiente_analito / self.coeficiente_titulante
        mols_analito = mols_titulante * fator
        return mols_analito / self.volume_amostra
