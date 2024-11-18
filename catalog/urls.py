from gettext import Catalog

from django.urls import path
from . import views  # Импортируем views
from .apps import CatalogConfig
from .views import CatalogListView, CatalogDetailView, ContactView


app_name = CatalogConfig.name

urlpatterns = [
    path('', views.product_list, name='product_list'),
    # path('', CatalogListView.as_view(), name='product_list'),  # Главная страница
    path('contact/', ContactView.as_view(), name='contact'),  # Страница контактов
    path('product/<int:pk>/',  CatalogDetailView.as_view(), name='product_detail'),
    path('product/new/', views.product_create, name='product_create'),
    path('product/<int:pk>/edit/', views.product_update, name='product_update'),
    path('product/<int:pk>/delete/', views.product_delete, name='product_delete'),
    path('product/<int:pk>/detail/', views.product_detail, name='product_detail')
]

