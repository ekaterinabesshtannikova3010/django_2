from gettext import Catalog

from django.urls import path
from . import views  # Импортируем views
from .apps import CatalogConfig
from .views import CatalogListView, CatalogDetailView, ContactView


app_name = CatalogConfig.name

urlpatterns = [
    path('', CatalogListView.as_view(), name='product_list'),  # Главная страница
    path('contact/', ContactView.as_view(), name='contact'),  # Страница контактов
    path('product/<int:pk>/',  CatalogDetailView.as_view(), name='product_detail'),
]
