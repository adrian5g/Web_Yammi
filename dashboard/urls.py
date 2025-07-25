from django.urls import path


from .views import home, registrar_restaurante, login_restaurante, logout_restaurante, listar_itens_cardapio, cadastrar_item_cardapio, editar_item_cardapio, remover_item_cardapio, listar_pedidos, info_home

urlpatterns = [
    path('', home),
    
    # AUTH
    path('cadastro/', registrar_restaurante, name='cadastro'),
    path('login/', login_restaurante, name='login'),
    path('logout/', logout_restaurante, name='logout'),

    # CRUD informações
    path('info/', info_home, name="home_info"),

    # CRUD pedidos
    path('pedidos/', listar_pedidos, name="listar_pedidos"),

    # CRUD Cardapio
    path('cardapio/', listar_itens_cardapio, name="listar_itens_cardapio"),
    path('cardapio_cadastrar/', cadastrar_item_cardapio, name="cadastrar_item_cardapio"),
    path('cardapio_editar/<int:id>/', editar_item_cardapio, name="editar_item_cardapio"),
    path('cardapio_remover/<int:id>/', remover_item_cardapio, name="remover_item_cardapio"),
]