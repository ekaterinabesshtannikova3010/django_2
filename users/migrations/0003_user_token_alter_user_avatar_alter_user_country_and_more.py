# Generated by Django 5.1.2 on 2024-11-17 17:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_remove_user_tg_name_user_country'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='token',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Token'),
        ),
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.ImageField(blank=True, help_text='Вставьте аватар', null=True, upload_to='users/avatars/', verbose_name='Аватар'),
        ),
        migrations.AlterField(
            model_name='user',
            name='country',
            field=models.CharField(blank=True, help_text='Введите свою страну', max_length=50, null=True, verbose_name='Страна'),
        ),
        migrations.AlterField(
            model_name='user',
            name='phone',
            field=models.CharField(blank=True, help_text='Введите номер телефона', max_length=30, null=True, verbose_name='Телефон'),
        ),
    ]