from django.shortcuts import render
from .models import Post


def tosh(request):
    lista = [
        'Django', 'Python', 'VSC', 
        'Git', 'Banco de Dados'
        ]
    lista_posts = Post.objects.all()
    data = {
        'erico':'Olá meu nome é Érico', 
        'lista_tecnologias': lista, 
        'posts': lista_posts
        }
    
    return render(request, 'index.html',data)

