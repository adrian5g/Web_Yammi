from django.contrib import admin
from .models import Restaurante, Usuario, ItemCardapio, Pedido, PedidoItem

class PedidoItemInline(admin.TabularInline):
    model = PedidoItem
    extra = 1 

class PedidoAdmin(admin.ModelAdmin):
    list_display = ('id', 'cliente_nome', 'status', 'data_hora', 'restaurante')
    list_editable = ('status',) 
    list_filter = ('status', 'data_hora', 'restaurante')
    search_fields = ('cliente_nome', 'id')
    inlines = [PedidoItemInline]

admin.site.register(Restaurante)
admin.site.register(Usuario)
admin.site.register(ItemCardapio)
admin.site.register(Pedido, PedidoAdmin) # Registra o Pedido com a configuração customizada
admin.site.register(PedidoItem)