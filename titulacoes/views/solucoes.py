from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def lista_solucoes(request):
    return render(request, 'solucoes/lista.html', {'solucoes': []})