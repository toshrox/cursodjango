from django.shortcuts import render


def tosh(request):
    return render(request, 'index.html')

