from django.db.models import Model
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from titulacoes.models import Experimento, SolucaoTitulante, Titulacao
from titulacoes.forms import ExperimentoForm, TitulacaoForm
from titulacoes.calculos import obter_calculadora
from titulacoes.calculos.estatistica import calcular_estatisticas

def _construir_contexto_lista(request, form = None):
    experimentos = Experimento.objects.filter(usuario = request.user)

    tipo_atual = request.GET.get('tipo', '')
    if tipo_atual:
        experimentos = experimentos.filter(tipo = tipo_atual)

    ordenar_atual = request.GET.get('ordenar', 'recente')
    if ordenar_atual == 'antigo':
        experimentos = experimentos.order_by('data_realizacao')
    else:
        experimentos = experimentos.order_by('-data_realizacao')

    return {
        'experimentos': experimentos,
        'tipo_choices': Experimento.TIPO_CHOICES,
        'tipo_atual': tipo_atual,
        'ordenar_atual': ordenar_atual,
        'form': form or ExperimentoForm(),
    }

@login_required
def lista_experimentos(request):
    context = _construir_contexto_lista(request)
    return render(request, 'experimentos/lista.html', context)

def criar_experimento(request):
    form = ExperimentoForm(request.POST)
    if form.is_valid():
        experimento = form.save(commit = False)
        experimento.usuario = request.user
        experimento.save()
        return redirect('experimento:lista')

def _construir_contexto_detalhe(request, experimento, form = None):
    titulacoes = experimento.titulacoes.all()
    return {
        'experimento': experimento,
        'titulacoes': titulacoes,
        'solucoes_titulantes': SolucaoTitulante.objects.filter(usuario=request.user),
        'estatisticas': calcular_estatisticas(titulacoes),
        'form': form or TitulacaoForm(usuario=request.user),
    }

@login_required
def detalhe_experimento(request, pk):
    experimento = get_object_or_404(Experimento, pk = pk, usuario = request.user)
    context = _construir_contexto_detalhe(request, experimento)
    return render(request, 'experimentos/detalhe.html', context)

@login_required
def registrar_titulacao(request, pk):
    experimento = get_object_or_404(Experimento, pk=pk, usuario = request.user)
    form = TitulacaoForm(request.POST, usuario=request.user)

    if form.is_valid():
        titulacao = form.save(commit=False)
        titulacao.experimento = experimento

        fator = titulacao.solucao_titulante.fator_correcao or 1
        concentracao_titulante = titulacao.solucao_titulante.concentracao_nominal * fator

        calculadora = obter_calculadora(
            experimento.tipo,
            titulacao.volume_titulante,
            titulacao.volume_amostra,
            concentracao_titulante,
            titulacao.coeficiente_titulante,
            titulacao.coeficiente_analito,
        )
        titulacao.concentracao_calculada = calculadora.calcular_concentracao()
        titulacao.save()
        return redirect('experimentos:detalhe', pk = pk)
    context = _construir_contexto_detalhe(request, experimento, form=form)
    return render(request, 'experimentos/detalhe.html', context)
