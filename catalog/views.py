from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProductForm
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product
from django.core.cache import cache


class ContactView(TemplateView):
    template_name = 'contact.html'


class CatalogDetailView(DetailView):
    model = Product


class CatalogListView(ListView):
    model = Product
    template_name = 'product_list.html'


class ProductListView(ListView):
    model = Product
    template_name = 'catalog/product_list.html'
    context_object_name = 'products'

    def get_queryset(self):
        queryset = cache.get('product_list')
        if not queryset:
            queryset = super().get_queryset()
            cache.set('product_list', queryset, 60 * 15)  # Кешируем данные на 15 минут
        return queryset


class ProductCreateView(LoginRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy('catalog:product_list')

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs['pk'])


class ProductDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_confirm_delete.html'
    context_object_name = 'product'
    success_url = reverse_lazy('catalog:product_list')
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        return get_object_or_404(Product, pk=self.kwargs['pk'])

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_staff


class ProductEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'edit_product.html'
    context_object_name = 'product'

    def test_func(self):
        product = self.get_object()
        return self.request.user == product.owner or self.request.user.is_staff

    def get_success_url(self):
        return reverse_lazy('product_list')


class UnpublishProductView(PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'
    raise_exception = True

    def post(self, pk):
        product = get_object_or_404(Product, pk=pk)
        product.published_status = False
        product.save()
        return redirect('catalog:product_list')


@method_decorator(cache_page(60 * 15), name='dispatch')  # Кешируем на 15 минут
class ProductDetailView(DetailView):
    model = Product
    template_name = 'catalog/product_detail.html'
