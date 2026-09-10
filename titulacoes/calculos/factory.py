from titulacoes.models import Experimento
from .acido_base import CalculadoraAcidoBase
from .redox import CalculadoraRedox
from .complexometrica import CalculadoraComplexometrica
from .precipitacao import CalculadoraPrecipitacao

#liga o valor salvo no campo 'tipo' com a calculadora correspondente
CALCULADORAS_POR_TIPO = {
    Experimento.TIPO_ACIDO_BASE: CalculadoraAcidoBase,
    Experimento.TIPO_REDOX: CalculadoraRedox,
    Experimento.TIPO_COMPLEXOMETRICA: CalculadoraComplexometrica,
    Experimento.TIPO_PRECIPITACAO: CalculadoraPrecipitacao,
}

def obter_calculadora(tipo, volume_titulante, volume_amostra, concentracao_titulante,
                      coeficiente_titulante=1, coeficiente_analito=1):
    classe = CALCULADORAS_POR_TIPO[tipo]
    return classe(volume_titulante, volume_amostra, concentracao_titulante,
                  coeficiente_titulante, coeficiente_analito,
    )