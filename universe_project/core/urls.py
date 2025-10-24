# universe_project/urls.py
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('cadastrar/', views.cadastrar_cliente, name='cadastrar_cliente'),
    path('editar/<int:pk>/', views.editar_cliente, name='editar_cliente'),
    path('excluir/<int:pk>/', views.excluir_cliente, name='excluir_cliente'),
]
