from django.shortcuts import render
from .models import Contato
from django.core.paginator import Paginator
from django.db.models import Q


def index(request):
    contatos = Contato.objects.order_by('-id').filter(mostrar = True)
    paginator = Paginator(contatos, 4) 

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
        'contatos' : contatos
    })

def detalhes(request, contato_id):
    contato = Contato.objects.get(id = contato_id)
    return render(request, 'contatos/detalhes.html', {
        'contato' : contato
    })

def busca(request):
    termo  = request.GET.get('termo')
    contatos = Contato.objects.order_by('-id').filter(
        Q(nome__icontains = termo), mostrar = True)
    
    paginator = Paginator(contatos, 20)
    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
        'contatos' : contatos
    })