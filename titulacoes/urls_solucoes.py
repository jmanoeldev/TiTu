from django.urls import path
from titulacoes import views
from titulacoes.urls_experimentos import urlpatterns

app_name = 'solucoes'

urlpatterns = [
path('', views.lista_solucoes, name='lista'),
]