from django.urls import path


from .views import home, registrar_restaurante, login_restaurante, logout_restaurante, listar_itens_cardapio, cadastrar_item_cardapio, editar_item_cardapio, remover_item_cardapio, listar_pedidos, cadastrar_pedido, editar_pedido, remover_pedido, info_home, detalhar_pedido, cadastrar_pedido_item, editar_pedido_item,remover_pedido_item, editar_informacoes

urlpatterns = [
    path('', home),
    
    # AUTH
    path('cadastro/', registrar_restaurante, name='cadastro'),
    path('login/', login_restaurante, name='login'),
    path('logout/', logout_restaurante, name='logout'),

    # CRUD informações
    path('info/', info_home, name="home_info"),
    path('info/editar/', editar_informacoes, name='editar_informacoes'),

    # CRUD pedidos
    path('pedidos/', listar_pedidos, name="listar_pedidos"),
    path('pedidos/cadastrar/', cadastrar_pedido, name="cadastrar_pedido"), 
    path('pedidos/editar/<int:id>/', editar_pedido, name="editar_pedido"),   
    path('pedidos/remover/<int:id>/', remover_pedido, name="remover_pedido"), 

    # CRUD PedidoItem 
    path('pedidos/<int:pedido_id>/', detalhar_pedido, name="detalhar_pedido"),
    path('pedidos/<int:pedido_id>/itens/cadastrar/', cadastrar_pedido_item, name="cadastrar_pedido_item"),
    path('pedidos/<int:pedido_id>/itens/editar/<int:item_id>/', editar_pedido_item, name="editar_pedido_item"),
    path('pedidos/<int:pedido_id>/itens/remover/<int:item_id>/', remover_pedido_item, name="remover_pedido_item"),
   
    # CRUD Cardapio
    path('cardapio/', listar_itens_cardapio, name="listar_itens_cardapio"),
    path('cardapio/cadastrar/', cadastrar_item_cardapio, name="cadastrar_item_cardapio"),
    path('cardapio/editar/<int:id>/', editar_item_cardapio, name="editar_item_cardapio"),
    path('cardapio/remover/<int:id>/', remover_item_cardapio, name="remover_item_cardapio"),
]