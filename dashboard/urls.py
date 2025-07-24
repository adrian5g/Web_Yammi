from django.urls import path


from .views import home, cadastro_restaurante_form, listar_itens_cardapio, cadastrar_item_cardapio, editar_item_cardapio, remover_item_cardapio

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro_restaurante_form, name="cadastrar_restaurante"),

    # CRUD Cardapio
    path('cardapio/', listar_itens_cardapio, name="listar_itens_cardapio"),
    path('cardapio_cadastrar/', cadastrar_item_cardapio, name="cadastrar_item_cardapio"),
    path('cardapio_editar/<int:id>/', editar_item_cardapio, name="editar_item_cardapio"),
    path('cardapio_remover/<int:id>/', remover_item_cardapio, name="remove_item_cardapio"),
]