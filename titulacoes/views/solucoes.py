from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from titulacoes.models import SolucaoTitulante

@login_required
def lista_solucoes(request):
    solucoes = SolucaoTitulante.objects.filter(usuario = request)
    return render(request, 'solucoes/lista.html', {'solucoes': []})