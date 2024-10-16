from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField()  # Описание

    def __str__(self):
        return f'{self.name}'


class Product(models.Model):
    name = models.CharField(max_length=250, verbose_name='Наименование')
    description = models.TextField()  # Описание
    image = models.ImageField(upload_to='images/', blank=True, null=True)  # Изображение
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # Категория
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Цена за покупку
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'
        ordering = ['name']

    def __str__(self):
        return f'{self.name}'
