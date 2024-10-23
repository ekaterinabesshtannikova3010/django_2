from django.shortcuts import render, get_object_or_404
from .models import Product


def contact(request):
    return render(request, 'contact.html')


def home(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'home.html', context)


def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    context = {'product': product}
    return render(request, 'product_detail.html', context)

def product_list(request):
    pass

def index(request):
    return render(request, 'base.html')