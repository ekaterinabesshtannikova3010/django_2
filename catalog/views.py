from django.views.generic import ListView, DetailView, TemplateView
from .models import Product


class ContactView(TemplateView):
    template_name = 'contact.html'


class CatalogDetailView(DetailView):
    model = Product


class CatalogListView(ListView):
    model = Product
    template_name = 'product_list.html'
