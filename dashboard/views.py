from django.shortcuts import render, redirect, get_object_or_404 
from .forms import ItemCardapioForm, RestauranteCreationForm, PedidoForm, PedidoItemForm, RestauranteEditForm
from .models import ItemCardapio, Restaurante, Pedido, PedidoItem
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User


def home(request):
    return redirect('listar_itens_cardapio') # TODO: redirecionar para outra página


# AUTH
# Registro, Login e Logout


def registrar_restaurante(request):
    if request.method == 'POST':
        form = RestauranteCreationForm(request.POST, request.FILES)
        if form.is_valid():
            senha = form.cleaned_data['senha']
            cnpj = form.cleaned_data['cnpj']

            user = User.objects.create_user(username=cnpj, password=senha)

            restaurante = form.save(commit=False)
            restaurante.user = user
            restaurante.save()

            login(request, user)
            return redirect('listar_itens_cardapio')
    else:
        form = RestauranteCreationForm()

    return render(request, 'auth/form_cadastro.html', {'form': form})


def login_restaurante(request):
    if request.method == 'POST':
        username = request.POST['username']
        senha = request.POST['password']

        user = authenticate(request, username=username, password=senha)
        if user is not None:
            login(request, user)
            return redirect('listar_itens_cardapio') 
        else:
            messages.error(request, 'Usuário ou senha inválidos.')

    return render(request, 'auth/form_login.html')


def logout_restaurante(request):
    logout(request)
    return redirect('login')


# CRUD
# INFORMAÇÕES
def editar_informacoes(request):
    restaurante = Restaurante.objects.get(user=request.user)
    form = RestauranteEditForm(request.POST or None, request.FILES or None, instance=restaurante)

    if form.is_valid():
        form.save()
        messages.success(request, 'informações atualizadas com sucesso!')
        return redirect('home_info')
    return render(request, 'info/form_info.html', {'form':form})

@login_required
def info_home(request):
    restaurante = Restaurante.objects.get(user=request.user)
    return render(request, 'info/home.html', {'restaurante': restaurante})



# CRUD
# PEDIDOS


@login_required
def listar_pedidos(request):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedidos = Pedido.objects.filter(restaurante=restaurante).order_by('-data_hora') # Ordena pelos mais recentes

    contexto = {
        'pedidos': pedidos
    }
    return render(request, 'pedidos/home.html', contexto)


@login_required
def cadastrar_pedido(request):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    form = PedidoForm(request.POST or None) # Não tem upload de arquivo para Pedido

    if form.is_valid():
        pedido = form.save(commit=False)
        pedido.restaurante = restaurante  # Associa o pedido ao restaurante logado
        pedido.save()
        messages.success(request, 'Pedido cadastrado com sucesso!')
        return redirect('listar_pedidos')

    contexto = {
        'form': form
    }
    return render(request, 'pedidos/form.html', contexto)


@login_required
def editar_pedido(request, id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=id)

    # Verifica se o pedido pertence ao restaurante logado
    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para editar este pedido.')
        return redirect('listar_pedidos')

    form = PedidoForm(request.POST or None, instance=pedido)

    if form.is_valid():
        form.save()
        messages.success(request, 'Pedido atualizado com sucesso!')
        return redirect('listar_pedidos')

    contexto = {
        'form': form
    }
    return render(request, 'pedidos/form.html', contexto)


@login_required
def remover_pedido(request, id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=id)

    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para remover este pedido.')
        return redirect('listar_pedidos')

    pedido.delete()

    return redirect('listar_pedidos')

# CRUD
# ITENS DO CARDAPIO


@login_required
def listar_itens_cardapio(request):
    restaurante = Restaurante.objects.get(user=request.user)
    itens_cardapio = ItemCardapio.objects.filter(restaurante=restaurante)

    contexto = {
        'itens_cardapio': itens_cardapio
    }

    return render(request, 'cardapio/home.html', contexto)


@login_required
def cadastrar_item_cardapio(request):
    restaurante = Restaurante.objects.get(user=request.user)
    form = ItemCardapioForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        item = form.save(commit=False)
        item.restaurante = restaurante 
        item.save()
        return redirect('listar_itens_cardapio')

    contexto = {
        'form': form
    }

    return render(request, 'cardapio/form.html', contexto)


@login_required
def editar_item_cardapio(request, id):

    item_cardapio = get_object_or_404(ItemCardapio, pk=id)
    restaurante = get_object_or_404(Restaurante, user=request.user)

    if item_cardapio.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para editar este item.')
        return redirect('listar_itens_cardapio')

    form = ItemCardapioForm(request.POST or None,
                            request.FILES or None, instance=item_cardapio)

    if form.is_valid():
        form.save()
        return redirect('listar_itens_cardapio')

    contexto = {
        'form': form
    }

    return render(request, 'cardapio/form.html', contexto)


@login_required
def remover_item_cardapio(request, id):
    item_cardapio = get_object_or_404(ItemCardapio, pk=id)
    restaurante = get_object_or_404(Restaurante, user=request.user)

    if item_cardapio.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para remover este item.')
        return redirect('listar_itens_cardapio')
        
    item_cardapio.delete()

    return redirect('listar_itens_cardapio')


# CRUD DE PEDIDOITEM


@login_required
def detalhar_pedido(request, pedido_id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para visualizar este pedido.')
        return redirect('listar_pedidos')

    itens_pedido = PedidoItem.objects.filter(pedido=pedido)

    for item in itens_pedido:
        item.valor_total = item.valor_unitario * item.quantidade 
    contexto = {
        'pedido': pedido,
        'itens_pedido': itens_pedido
    }
    return render(request, 'pedidos/detalhe.html', contexto)


@login_required
def cadastrar_pedido_item(request, pedido_id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=pedido_id)

    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para adicionar itens a este pedido.')
        return redirect('listar_pedidos')

    form = PedidoItemForm(request.POST or None)

    form.fields['item_cardapio'].queryset = ItemCardapio.objects.filter(restaurante=restaurante)

    if form.is_valid():
        pedido_item = form.save(commit=False)
        pedido_item.pedido = pedido
        
        pedido_item.valor_unitario = pedido_item.item_cardapio.valor
        pedido_item.save()
        messages.success(request, 'Item adicionado ao pedido com sucesso!')
        return redirect('detalhar_pedido', pedido_id=pedido.id)

    contexto = {
        'form': form,
        'pedido': pedido
    }
    return render(request, 'pedidos/item_form.html', contexto)


@login_required
def editar_pedido_item(request, pedido_id, item_id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido_item = get_object_or_404(PedidoItem, pk=item_id, pedido=pedido)

    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para editar este item de pedido.')
        return redirect('listar_pedidos')

    form = PedidoItemForm(request.POST or None, instance=pedido_item)

    form.fields['item_cardapio'].queryset = ItemCardapio.objects.filter(restaurante=restaurante)

    if form.is_valid():
        if pedido_item.item_cardapio != form.cleaned_data['item_cardapio']:
             pedido_item.valor_unitario = form.cleaned_data['item_cardapio'].valor
        
        form.save()
        messages.success(request, 'Item do pedido atualizado com sucesso!')
        return redirect('detalhar_pedido', pedido_id=pedido.id)

    contexto = {
        'form': form,
        'pedido': pedido
    }
    return render(request, 'pedidos/item_form.html', contexto)


@login_required
def remover_pedido_item(request, pedido_id, item_id):
    restaurante = get_object_or_404(Restaurante, user=request.user)
    pedido = get_object_or_404(Pedido, pk=pedido_id)
    pedido_item = get_object_or_404(PedidoItem, pk=item_id, pedido=pedido)

    if pedido.restaurante != restaurante:
        messages.error(request, 'Você não tem permissão para remover este item de pedido.')
        return redirect('listar_pedidos')

    if request.method == 'POST':
        pedido_item.delete()
        messages.success(request, 'Item do pedido removido com sucesso!')
        return redirect('detalhar_pedido', pedido_id=pedido.id)
    
    messages.warning(request, 'Confirme a remoção do item do pedido.')
    return redirect('detalhar_pedido', pedido_id=pedido.id)

