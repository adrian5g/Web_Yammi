from django.db import models

# Create your models here.

from django.db import models

class Restaurante(models.Model):
    nome = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=18, unique=True) # CNPJ formatado: XX.XXX.XXX/XXXX-XX
    telefone = models.CharField(max_length=15) # Formato: (XX) XXXXX-XXXX
    email = models.EmailField(unique=True)
    imagem_url = models.URLField(max_length=200, blank=True, null=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome

class Usuario(models.Model):
    TIPO_USUARIO_CHOICES = [
        ('dono', 'Dono'),
        ('gerente', 'Gerente'),
        ('garcom', 'Garçom'),
    ]

    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    senha = models.CharField(max_length=128)
    tipo = models.CharField(max_length=10, choices=TIPO_USUARIO_CHOICES)
    imagem_url = models.URLField(max_length=200, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='usuarios')
    ativo = models.BooleanField(default=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"

class ItemCardapio(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    imagem_url = models.URLField(max_length=200, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='cardapio')

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
    status = models.CharField(max_length=20, choices=STATUS_PEDIDO_CHOICES, default='pendente')
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE, related_name='pedidos')
    # O usuário que registrou o pedido. Pode ser nulo se o pedido for feito por um sistema externo, por exemplo.
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True, related_name='pedidos_registrados')

    def __str__(self):
        return f"Pedido #{self.id} - {self.cliente_nome}"

class PedidoItem(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name='itens')
    item_cardapio = models.ForeignKey(ItemCardapio, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField(default=1)
    
    valor_unitario = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.quantidade}x {self.item_cardapio.nome} no Pedido #{self.pedido.id}"