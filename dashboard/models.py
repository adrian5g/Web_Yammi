from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Restaurante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True)
    telefone = models.CharField(max_length=15)
    imagem = models.ImageField(upload_to='restaurante/', null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem = models.ImageField(upload_to='cardapio/', blank=False, null=True)
    restaurante = models.ForeignKey(
        Restaurante, on_delete=models.CASCADE, related_name='cardapio')

    def __str__(self):
        return self.nome


class Pedido(models.Model):
    STATUS_PEDIDO_CHOICES = [
        ('pendente', 'Pendente'),
        ('em_preparo', 'Em Preparo'),
        ('a_caminho', 'A Caminho'),
        ('entregue', 'Entregue'),
        ('cancelado', 'Cancelado'),
    ]

    cliente_nome = models.CharField(max_length=255)
    cliente_endereco = models.CharField(max_length=255)
    cliente_telefone = models.CharField(max_length=20)
    data_hora = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20, choices=STATUS_PEDIDO_CHOICES, default='pendente')
    restaurante = models.ForeignKey(
        Restaurante, on_delete=models.CASCADE, related_name='pedidos')

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nome}"


class PedidoItem(models.Model):
    pedido = models.ForeignKey(
        Pedido, on_delete=models.CASCADE, related_name='itens')
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)

    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.item_cardapio.nome} no Pedido #{self.pedido.id}"
