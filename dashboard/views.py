from django.shortcuts import render, redirect
from .forms import RestauranteForm, ItemCardapioForm
from .models import ItemCardapio
from .fake_session import get_logged_restaurante


def home(request):
    return render(request, 'home.html')


def cadastro_restaurante_form(request):
    form = RestauranteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        # return redirect('listar_acao')

    contexto = {
        'form': form
    }

    return render(request, 'cadastro_restaurante_form.html', contexto)


# CRUD
# ITENS DO CARDAPIO

def listar_itens_cardapio(request):
    restaurante = get_logged_restaurante()  # TODO: realmente pegar da sessão
    itens_cardapio = ItemCardapio.objects.filter(restaurante=restaurante)

    contexto = {
        'itens_cardapio': itens_cardapio
    }

    return render(request, 'cardapio/home.html', contexto)


def cadastrar_item_cardapio(request):
    restaurante = get_logged_restaurante()  # TODO: realmente pegar da sessão
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


def editar_item_cardapio(request, id):
    # TODO: editar somente se o restaurante em do item for o mesmo da sessão

    item_cardapio = ItemCardapio.objects.get(pk=id)

    form = ItemCardapioForm(request.POST or None, request.FILES or None, instance=item_cardapio)

    if form.is_valid():
        form.save()
        return redirect('listar_itens_cardapio')

    contexto = {
        'form': form
    }

    return render(request, 'cardapio/form.html', contexto)


def remover_item_cardapio(request, id):
    # TODO: remover somente se o restaurante em do item for o mesmo da sessão

    item_cardapio = ItemCardapio.objects.get(pk=id)
    item_cardapio.delete()

    return redirect('listar_itens_cardapio')
