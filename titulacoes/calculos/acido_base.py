from .base import CalculadoraTitulacao

class CalculadoraAcidoBase(CalculadoraTitulacao):
    fator_estequiometrico = 1

    def calcular_concentracao(self):
        pass
