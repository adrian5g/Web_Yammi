from .models import Restaurante, ItemCardapio, Pedido, PedidoItem
from django import forms

class RestauranteCreationForm(forms.ModelForm):
    senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': 'Digite sua senha'})
    )
    confirmar_senha = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'input-form', 'placeholder': 'Confirme sua senha'})
    )

    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone', 'imagem', 'senha', 'confirmar_senha']

    def clean(self):
        cleaned_data = super().clean()
        senha = cleaned_data.get("senha")
        confirmar = cleaned_data.get("confirmar_senha")

        if senha != confirmar:
            raise forms.ValidationError("As senhas não coincidem.")
        
        return cleaned_data



class ItemCardapioForm(forms.ModelForm):
    class Meta:
        model = ItemCardapio
        fields = ['nome', 'descricao', 'valor', 'imagem', 'imagem']


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente_nome', 'cliente_endereco', 'cliente_telefone', 'status']



class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ['item_cardapio', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        