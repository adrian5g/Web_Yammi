from django.forms import ModelForm
from .models import Restaurante

class RestauranteForm(ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone', 'email', 'imagem', 'senha']