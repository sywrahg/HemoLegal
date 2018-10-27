from django.conf.urls import url
from django.urls import path, include
from django.contrib import admin
from . import views

app_name = 'core'

urlpatterns = [
	path('', views.Home.as_view(),name='home'),
	path('cadastro_doador/', views.CadastroDoador.as_view(),name='cadastro_doador'),
	path('doadores/', views.ListarDoadores.as_view(),name='doadores'),
    path('detalhe_doador/<int:doador_id>', views.DetalheDoador.as_view(), name='detalhe_doador'),
    path('detalhe_doacao/<int:doacao_id>', views.DetalheDoacao.as_view(), name='detalhe_doacao'),
]