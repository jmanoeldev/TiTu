from multiprocessing import context

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

import titulacoes
from titulacoes.models import Experimento, Titulacao, SolucaoTitulante

@login_required
def lista_experimentos(request):
    experimentos = Experimento.objects.filter(usuario = request.user)
    tipo_atual = request.GET.get('tipo', '')
    if tipo_atual:
        experimentos = experimentos.filter(tipo = tipo_atual)

    ordenar_atual = request.GET.get('ordenar', 'recente')
    if ordenar_atual == 'antigo':
        experimentos = experimentos.order_by('data_realizacao')
    else:
        experimentos = experimentos.order_by('-data_realizacao')

    context = {
        'experimentos': experimentos,
        'tipo_choices': Experimento.TIPO_CHOICES,
        'tipo_atual': tipo_atual,
        'ordenar_atual': ordenar_atual,
    }
    return render(request, 'experimentos/lista.html', context)
def criar_experimento(request):
    #temporario
    return redirect('experimentos:lista')

@login_required
def detalhe_experimento(request, pk):
    experimento = get_object_or_404(Experimento, pk = pk, usuario = request.user)
    titulacoes = experimento.titulacoes.all()
    solucoes_titulantes = SolucaoTitulante.objects.filter(usuario = request.user)

    estatisticas = {
        'media' : None,
        'desvio_padrao': None,
        'q_calculado': None,
        'outlier_id': None,
    }

    context = {
        'experimento': experimento,
        'titulacoes': titulacoes,
        'solucoes_titulantes': solucoes_titulantes,
        'estatisticas': estatisticas,
    }
    return render(request, 'experimentos/detalhe.html', context)

@login_required
def registrar_titulacao(request, pk):
    return redirect('experimentos:detalhe', pk = pk)