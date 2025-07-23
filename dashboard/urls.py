from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import home, cadastro_restaurante_form

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro_restaurante_form, name="cadastrar_restaurante"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)