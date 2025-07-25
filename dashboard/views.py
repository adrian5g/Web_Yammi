from django.shortcuts import render, redirect
from .forms import ItemCardapioForm, RestauranteCreationForm
from .models import ItemCardapio, Restaurante
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


@login_required
def info_home(request):
    return render(request, 'info/home.html')


# CRUD
# PEDIDOS


@login_required
def listar_pedidos(request):
    return render(request, 'pedidos/home.html')

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
        item.restaurante = restaurante  # define o restaurante antes de salvar
        item.save()
        return redirect('listar_itens_cardapio')

    contexto = {
        'form': form
    }

    return render(request, 'cardapio/form.html', contexto)


@login_required
def editar_item_cardapio(request, id):
    # TODO: editar somente se o restaurante em do item for o mesmo da sessão

    item_cardapio = ItemCardapio.objects.get(pk=id)

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
    # TODO: remover somente se o restaurante em do item for o mesmo da sessão

    item_cardapio = ItemCardapio.objects.get(pk=id)
    item_cardapio.delete()

    return redirect('listar_itens_cardapio')
