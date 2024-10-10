from gettext import Catalog

from django.urls import path
from . import views  # Импортируем views
from .apps import CatalogConfig

app_name = CatalogConfig.name

urlpatterns = [
    path('', views.home, name='home'),          # Главная страница
    path('contact/', views.contact, name='contact'),  # Страница контактов
]