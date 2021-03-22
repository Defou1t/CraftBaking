from django.shortcuts import render
from .models import Products


def index(request):
    products = Products.objects.all()
    return render(request, 'handmadeapp/index.html', {'title':'Главная страница сайта', 'products': products})

def about(request):
    return render(request, 'handmadeapp/about.html')