# core/views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages  # usar para mostrar mensagens ao usuário
from .models import Cliente
from .forms import ClienteForm


# ---------------------------
# Função: index
# ---------------------------
# O que eu quero dizer aqui em palavras simples:
# - Quando alguém abre a página inicial, eu preciso mostrar a lista
#   completa de clientes e também deixar um formulário pronto para o
#   modal de cadastro/edição. Essa função apenas prepara esses dados
#   e devolve para o template.
def index(request):
    clientes = Cliente.objects.all()  # pega todos os clientes do banco
    form = ClienteForm()  # formulário vazio para usar no modal
    # Renderiza 'index.html' com a lista e o formulário
    return render(request, 'index.html', {'clientes': clientes, 'form': form})


# ---------------------------
# Função: cadastrar_cliente
# ---------------------------
# Explicação simples:
# - Recebe os dados do formulário de cadastro (quando o usuário clica em
#   salvar no modal). Se tudo estiver ok, salva o cliente e mostra uma
#   mensagem de sucesso. Se tiver erro de validação, devolve a página
#   com o formulário preenchido com erros para que o modal reabra.
def cadastrar_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            # Mensagem curta para o usuário (aparecerá como toast)
            messages.success(request, 'Cliente cadastrado com sucesso!')
            return redirect('index')
        else:
            # Se o formulário tiver erro, renderizamos a mesma página com
            # o formulário já contendo os erros. O template/JS usa a
            # variável 'erros_cadastro' para reabrir o modal automaticamente.
            clientes = Cliente.objects.all()
            return render(request, 'index.html', {
                'clientes': clientes,
                'form': form,
                'erros_cadastro': True,
            })
    # Se alguém acessar via GET, apenas volta para a lista
    return redirect('index')


# ---------------------------
# Função: editar_cliente
# ---------------------------
# Explicação simples:
# - Atualiza os dados de um cliente já existente. Recebe o id (pk) e os
#   novos valores. Se der certo, salva e mostra mensagem de sucesso. Se
#   houver erro, devolve a página com o formulário com erros e indica ao
#   JS que reabra o modal de edição.
def editar_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente "{cliente.nome}" alterado com sucesso!')
            return redirect('index')
        else:
            clientes = Cliente.objects.all()
            return render(request, 'index.html', {
                'clientes': clientes,
                'form': form,
                'erros_edicao': True,
                'pk_erro_edicao': pk,
            })
    return redirect('index')


# ---------------------------
# Função: excluir_cliente
# ---------------------------
# Explicação simples:
# - Recebe um POST confirmando a exclusão. Antes de apagar guardamos o
#   nome para mostrar na mensagem. Depois redirecionamos para a lista.
def excluir_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        nome_cliente = cliente.nome
        cliente.delete()
        messages.warning(request, f'Cliente "{nome_cliente}" excluído permanentemente.')
        return redirect('index')
    return redirect('index')