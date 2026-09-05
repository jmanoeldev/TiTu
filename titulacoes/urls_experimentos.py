from django.urls import path
from titulacoes import views

app_name = 'experimentos'

urlpatterns = [
    path('', views.lista_experimentos, name='lista'),
    path('novo/', views.criar_experimento, name='criar'),
]