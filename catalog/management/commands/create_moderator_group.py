from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = 'Создает группу модераторов продуктов и назначает права'

    def handle(self, *args, **kwargs):
        moderator_group, created = Group.objects.get_or_create(name='Модератор продуктов')

        permission = Permission.objects.get(codename='can_unpublish_product', content_type__model='product')

        moderator_group.permissions.add(permission)

        delete_permission = Permission.objects.get(codename='delete_product', content_type__model='product')
        moderator_group.permissions.add(delete_permission)

        self.stdout.write(self.style.SUCCESS('Группа "Модератор продуктов" успешно создана и настроена.'))