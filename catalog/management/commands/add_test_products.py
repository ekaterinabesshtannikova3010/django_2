from django.core.management.base import BaseCommand
from catalog.models import Category, Product


class Command(BaseCommand):
    help = 'Add test products to the database'

    def handle(self, *args, **kwargs):
        # Удаляем все данные из таблиц Product и Category
        Product.objects.all().delete()
        Category.objects.all().delete()

        # Создаем тестовые категории
        category1 = Category.objects.create(name='Electronics')
        category2 = Category.objects.create(name='Books')

        # Создаем тестовые продукты
        Product.objects.create(name='Smartphone', category=category1, price=699.99)
        Product.objects.create(name='Laptop', category=category1, price=999.99)
        Product.objects.create(name='Fiction Novel', category=category2, price=19.99)
        Product.objects.create(name='Science Book', category=category2, price=29.99)

        self.stdout.write(self.style.SUCCESS('Successfully added test products'))
