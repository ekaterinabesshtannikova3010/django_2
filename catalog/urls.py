from gettext import Catalog

from django.urls import path
from . import views  # Импортируем views
from .apps import CatalogConfig
from .views import product_detail, product_list
from catalog.views import index

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),  # Главная страница
    path('contact/', views.contact, name='contact'),  # Страница контактов
    path('product/<int:pk>/', product_detail, name='product_detail'),
    path('products/', product_list, name='product_list'),
]
