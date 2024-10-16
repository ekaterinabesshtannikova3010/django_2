from django.shortcuts import render


def contact(request):
    return render(request, 'catalog/contact.html')


def home(request):
    return render(request, 'catalog/home.html')
