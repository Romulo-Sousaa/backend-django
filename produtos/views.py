from django.shortcuts import render, get_object_or_404, redirect
from .models import Produto, Cliente, Venda
from .forms import ProdutoForm, ClienteForm, VendaForm

#Produto
# Listagem
def lista_produtos(request):
    produtos = Produto.objects.all()
    clientes = Cliente.objects.all()
    vendas = Venda.objects.all()
    return render(request, 'produtos/list_produtos.html', {
        'produtos': produtos,
        'clientes': clientes,
        'vendas': vendas
    })

# Criação
def cria_produto(request):
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm()
    return render(request, 'produtos/form_produto.html', {'form': form})

# Edição
def edita_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ProdutoForm(instance=produto)
    return render(request, 'produtos/form_produto.html', {'form': form})

# Remoção
def remove_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete_produto.html', {'produto': produto})

def detalhe_produto(request, pk):
    produto = get_object_or_404(Produto, pk=pk)
    return render(request, 'produtos/detalhe_produto.html', {'produto': produto})



# Cliente
# Listagem
def lista_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'produtos/list_produtos.html', {'clientes': clientes})

# Criação
def cria_cliente(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ClienteForm()
    return render(request, 'produtos/form_cliente.html', {'form': form})

# Edição
def edita_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'produtos/form_cliente.html', {'form': form})

# Remoção
def remove_cliente(request, pk):
    cliente = get_object_or_404(Cliente, pk=pk)
    if request.method == 'POST':
        cliente.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete_cliente.html', {'cliente': cliente})



# Venda
# Criação
def cria_venda(request):
    if request.method == 'POST':
        form = VendaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = VendaForm()
    return render(request, 'produtos/form_venda.html', {'form': form})

# Edição
def edita_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        form = VendaForm(request.POST, instance=venda)
        if form.is_valid():
            form.save()
            return redirect('lista_produtos')
    else:
        form = VendaForm(instance=venda)
    return render(request, 'produtos/form_venda.html', {'form': form})

# Remoção
def remove_venda(request, pk):
    venda = get_object_or_404(Venda, pk=pk)
    if request.method == 'POST':
        venda.delete()
        return redirect('lista_produtos')
    return render(request, 'produtos/confirm_delete_venda.html', {'venda': venda})

# Listagem de vendas
def venda_list(request):
    vendas = Venda.objects.all()
    clientes = Cliente.objects.all()
    cliente_id = request.GET.get('cliente')
    data_inicio = request.GET.get('data_inicio')
    data_fim = request.GET.get('data_fim')

    if cliente_id:
        vendas = vendas.filter(cliente_id=cliente_id)
        cliente_id = int(cliente_id)

    if data_inicio and data_fim:
        vendas = vendas.filter(data_venda__range=[data_inicio, data_fim])

    return render(request, 'produtos/vendas_list.html', {
        'vendas': vendas,
        'clientes': clientes,
        'cliente_id': cliente_id,
        'data_inicio': data_inicio,
        'data_fim': data_fim,
    })