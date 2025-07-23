from django.shortcuts import render
from .forms import RestauranteForm
def home(request):
  return render(request, 'home.html')

def cadastro_restaurante_form(request):
    form = RestauranteForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        # return redirect('listar_acao')

    contexto = {
        'form': form
    }
    
    return render(request, 'cadastro_restaurante_form.html', contexto)