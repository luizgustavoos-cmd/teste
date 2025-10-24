# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente
from .forms import ClienteForm

def index(request):
    clientes = Cliente.objects.all()
    return render(request, 'index.html', {'clientes': clientes})

def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm()
    return render(request, 'cadastro.html', {'form': form})

def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'cadastro.html', {'form': form, 'editar': True})

def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('index')
    return render(request, 'confirmar_exclusao.html', {'cliente': cliente})
