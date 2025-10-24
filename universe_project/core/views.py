# # core/views.py
# from django.shortcuts import render
# # Lembre-se, use o nome da classe correto: Cliente
# from .models import Cliente 

# def index(request):
#     # CORREÇÃO 1: Precisa do método .all() para buscar todos os objetos
#     clientes = Cliente.objects.all() 
    
#     # CORREÇÃO 2: A função render() é chamada com parênteses, não chaves.
#     context = {'clientes': clientes}
    
#     # Renderiza o template 'index.html' passando o dicionário de contexto.
#     return render(request, 'index.html', context)


# core/views.py
# from django.shortcuts import render, redirect
# from .models import Cliente
# from .forms import ClienteForm  # vamos criar o forms.py se ainda não existir

# def index(request):
#     # Busca todos os clientes do banco
#     clientes = Cliente.objects.all().order_by('nome')

#     # Instancia o formulário vazio
#     form = ClienteForm()

#     # Se o formulário foi enviado (método POST)
#     if request.method == 'POST':
#         form = ClienteForm(request.POST)
#         if form.is_valid():
#             form.save()
#             # Após salvar, redireciona para evitar reenvio de formulário
#             return redirect('index')

#     # Contexto com lista e formulário
#     context = {'clientes': clientes, 'form': form}

#     # Renderiza o template index.html com os dados
#     return render(request, 'index.html', context)


from django.shortcuts import render, redirect
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
