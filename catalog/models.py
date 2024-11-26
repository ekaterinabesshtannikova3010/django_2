from django.db import models

from users.models import User


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField()  # Описание

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    objects = None
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField()  # Описание
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Изображение
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за покупку
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения
    published_status = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        permissions = [
            ("can_unpublish_product", "Can unpublish product"),
        ]

    def __str__(self):
        return f'{self.name}'
