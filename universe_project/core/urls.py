"""
URL configuration for the `core` app.

Nota rápida (linguagem simples): aqui eu declaro os endereços (rotas)
que o aplicativo usa. Cada rota aponta para uma função que roda no
servidor (essas funções estão em `core/views.py`).

Exemplo: a rota `cadastrar/` é usada quando o formulário de cadastro
é submetido. Não colocamos a rota do `admin/` aqui porque o arquivo
principal do projeto já cuida disso.
"""
from django.urls import path
from . import views

urlpatterns = [
    # Página principal — lista todos os clientes
    path('', views.index, name='index'),

    # Cadastrar um novo cliente (espera POST)
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),

    # Editar um cliente existente; <int:pk> é o id do cliente
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),

    # Excluir um cliente (confirmação via modal)
    path('excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]
