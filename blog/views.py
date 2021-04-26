from django.shortcuts import render


# Create your views here.
def render_index(request):
    nome = 'Raimundo'
    return render(request, 'index.html', {'nome': nome})
