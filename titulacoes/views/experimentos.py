from multiprocessing import context

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def lista_experimentos(request):
    context = {
        'experimentos': [],
        'tipo_choices': [],
        'tipo_atual': request.GET.get('tipo', ''),
        'ordenar_atual': request.GET.get('ordenar', 'recente')
    }
    return render(request, 'experimentos/lista.html', context)
def criar_experimento(request):
    #temporario
    return redirect('experimentos:lista')