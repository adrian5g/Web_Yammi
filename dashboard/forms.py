from django.forms import ModelForm
from .models import Restaurante, ItemCardapio


class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone', 'email', 'imagem', 'senha']


class ItemCardapioForm(ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ['nome', 'descricao', 'valor', 'imagem', 'imagem']
