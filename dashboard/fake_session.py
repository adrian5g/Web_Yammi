from .models import ItemCardapio, Restaurante
from .fake_session import get_logged_restaturante_id

def get_logged_restaurante_id():
  return 1

def get_logged_restaurante():
  restaurante_id = get_logged_restaurante_id()

  return Restaurante.objects.get(pk=restaurante_id)