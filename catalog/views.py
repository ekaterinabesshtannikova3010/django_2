from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .forms import ProductForm
from django.views import View
from django.contrib.auth.mixins import PermissionRequiredMixin
from .models import Product

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

    # def post(self, request, pk):
    #     product = get_object_or_404(Product, pk=pk)
    #     product.delete()
    #     return redirect('catalog:product_list')

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

@login_required
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'catalog/product_detail.html', {'product': product})
