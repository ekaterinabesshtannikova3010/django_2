# Generated by Django 5.1.2 on 2024-11-21 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_alter_product_options_product_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='status',
        ),
        migrations.AddField(
            model_name='product',
            name='published_status',
            field=models.BooleanField(default=False),
        ),
    ]