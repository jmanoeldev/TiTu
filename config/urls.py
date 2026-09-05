from tempfile import template

from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from titulacoes import views as titulacoes_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', titulacoes_views.home, name = 'home'),
    path('cadastro/', titulacoes_views.cadastro, name = 'cadastro'),

    path('login/', auth_views.LoginView.as_view(template_name = 'login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(next_page = 'home'), name = 'logout'),

    path('experimentos/', include('titulacoes.urls_experimentos')),
    path('solucoes/', include('titulacoes.urls_solucoes'))
]
