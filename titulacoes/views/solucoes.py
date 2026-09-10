from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from titulacoes.models import SolucaoTitulante
from  titulacoes.forms import SolucaoTitulanteForm

@login_required
def lista_solucoes(request):
    if request.method == 'POST':
        form = SolucaoTitulanteForm(request.POST)
        if form.is_valid():
            solucao = form.save(commit=False)
            solucao.usuario = request.user
            solucao.save()
            return redirect('solucoes:lista')
    else:
        form = SolucaoTitulanteForm()

    solucoes = SolucaoTitulante.objects.filter(usuario=request.user)
    return render(request, 'solucoes/lista.html', {'solucoes': solucoes, 'form': form})