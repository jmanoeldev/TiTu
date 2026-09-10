from statistics import mean, stdev

#Valores criticos do teste Q de Dixon, nivel de confiança: 90%
_Q_CRITICO_90 = {
    3: 0.94, 4: 0.76, 5: 0.64, 6: 0.56,
    7: 0.51, 8: 0.47, 9: 0.44, 10: 0.41,
}

def _teste_q(valores_ordenados):
    intervalo = valores_ordenados[-1] - valores_ordenados[0]
    if intervalo == 0:
        return None, None

    gap_menor = valores_ordenados[1] - valores_ordenados[0]
    gap_maior = valores_ordenados[-1] - valores_ordenados[-2]

    if gap_menor >= gap_maior:
        return round(gap_menor / intervalo, 4), valores_ordenados[0]
    return round(gap_maior / intervalo, 4), valores_ordenados[-1]

def calcular_estatisticas(titulacoes):
    pares = [
        (t.id, t.concentracao_calculada)
        for t in titulacoes if t.concentracao_calculada is not None
    ]

    if len(pares) < 2:
        return {'media': None, 'desvio_padrao': None, 'q_calculado': None, 'outlier_id': None}

    valores = [v for _, v in pares]
    media = mean(valores)
    desvio_padrao = stdev(valores)

    q_calculado = None
    outlier_id = None

    if len(pares) >= 3:
        pares_ordenados = sorted(pares, key=lambda par: par[1])
        valores_ordenados = [v for _, v in pares_ordenados]
        q_calculado, valor_suspeito = _teste_q(valores_ordenados)

        q_critico = _Q_CRITICO_90.get(len(pares))
        if q_calculado is not None and q_critico is not None and q_calculado > q_critico:
            for id_titulacao, valor in pares_ordenados:
                if valor == valor_suspeito:
                    outlier_id = id_titulacao
                    break
        return  {
            'media': media,
            'desvio_padrao': desvio_padrao,
            'q_calculado': q_calculado,
            'outlier_id': outlier_id,
        }