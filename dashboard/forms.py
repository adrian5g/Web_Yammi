from .models import Restaurante, ItemCardapio, Pedido, PedidoItem
from django import forms


class RestauranteCreationForm(forms.ModelForm):
    senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Senha'}))
    confirmar_senha = forms.CharField(widget=forms.PasswordInput(
        attrs={'placeholder': 'Confirmar senha'}))

    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone',
                  'imagem', 'senha', 'confirmar_senha']
        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'CNPJ'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'imagem': forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'

    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone',
                  'imagem', 'senha', 'confirmar_senha']

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente_nome', 'cliente_endereco',
                  'cliente_telefone', 'status']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class PedidoItemForm(forms.ModelForm):
    class Meta:
        model = PedidoItem
        fields = ['item_cardapio', 'quantidade']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'


class RestauranteEditForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ['nome', 'cnpj', 'telefone', 'imagem']

        widgets = {
            'nome': forms.TextInput(attrs={'placeholder': 'Nome'}),
            'cnpj': forms.TextInput(attrs={'placeholder': 'CNPJ'}),
            'telefone': forms.TextInput(attrs={'placeholder': 'Telefone'}),
            'imagem': forms.ClearableFileInput(),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-input'
