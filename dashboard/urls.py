from django.urls import path


from .views import home, registrar_restaurante, login_restaurante, logout_restaurante, listar_itens_cardapio, cadastrar_item_cardapio, editar_item_cardapio, remover_item_cardapio

urlpatterns = [
    path('', home),
    
    path('registro/', registrar_restaurante, name='registro'),
    path('login/', login_restaurante, name='login'),
    path('logout/', logout_restaurante, name='logout'),

    # CRUD Cardapio
    path('cardapio/', listar_itens_cardapio, name="listar_itens_cardapio"),
    path('cardapio_cadastrar/', cadastrar_item_cardapio, name="cadastrar_item_cardapio"),
    path('cardapio_editar/<int:id>/', editar_item_cardapio, name="editar_item_cardapio"),
    path('cardapio_remover/<int:id>/', remover_item_cardapio, name="remove_item_cardapio"),
]