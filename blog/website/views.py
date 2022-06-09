from django.shortcuts import render


def tosh(request):
    lista = [
        'Django', 'Python', 'VSC', 
        'Git', 'Banco de Dados'
        ]
    data = {'erico':'Olá meu nome é Érico', 'mariana': 'E eu sou a Mariana', 'lista_tecnologias': lista}
    
    return render(request, 'index.html',data)

