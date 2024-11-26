
from django.urls import path
from . import views
from .apps import CatalogConfig
from .views import ProductListView, ContactView, ProductUpdateView, ProductDeleteView, \
    UnpublishProductView, ProductDetailView
from .views import ProductCreateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', ProductListView.as_view(), name='product_list'),# Главная страница
    # path('products/category/<int:pk>/', ProductListView.as_view(), name='product_list'),
    path('contact/', ContactView.as_view(), name='contact'),  # Страница контактов
    # path('product/<int:pk>/',  CatalogDetailView.as_view(), name='product_detail'),
    path('product/create/',ProductCreateView.as_view(), name='product_create'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
    path('product/<int:pk>/detail/',ProductDetailView.as_view(), name='product_detail'),
    path('product/<int:product_id>/unpublish/', UnpublishProductView.as_view(), name='unpublish_product'),
]

