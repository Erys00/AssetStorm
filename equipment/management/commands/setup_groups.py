from django.core.management.base import BaseCommand
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from equipment.models import Equipment, EquipmentTransfer


class Command(BaseCommand):
    help = 'Tworzy grupy użytkowników i przypisuje im uprawnienia'

    def handle(self, *args, **options):
        # Pobierz content types
        equipment_ct = ContentType.objects.get_for_model(Equipment)
        transfer_ct = ContentType.objects.get_for_model(EquipmentTransfer)

        # Utwórz grupę IT
        it_group, created = Group.objects.get_or_create(name='IT')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Utworzono grupę IT')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Grupa IT już istnieje')
            )

        # Utwórz grupę normal_user
        normal_user_group, created = Group.objects.get_or_create(name='normal_user')
        if created:
            self.stdout.write(
                self.style.SUCCESS('Utworzono grupę normal_user')
            )
        else:
            self.stdout.write(
                self.style.WARNING('Grupa normal_user już istnieje')
            )

        # Przypisz uprawnienia do grupy IT
        it_permissions = [
            'add_equipment',
            'change_equipment', 
            'delete_equipment',
            'view_equipment',
            'add_equipmenttransfer',
            'change_equipmenttransfer',
            'delete_equipmenttransfer',
            'view_equipmenttransfer',
        ]

        for perm_name in it_permissions:
            if 'equipment' in perm_name:
                perm, created = Permission.objects.get_or_create(
                    codename=perm_name,
                    content_type=equipment_ct,
                    defaults={'name': f'Can {perm_name.replace("_", " ")}'}
                )
            else:
                perm, created = Permission.objects.get_or_create(
                    codename=perm_name,
                    content_type=transfer_ct,
                    defaults={'name': f'Can {perm_name.replace("_", " ")}'}
                )
            
            it_group.permissions.add(perm)

        # Przypisz uprawnienia do grupy normal_user (tylko podgląd)
        normal_user_permissions = [
            'view_equipment',
            'view_equipmenttransfer',
        ]

        for perm_name in normal_user_permissions:
            if 'equipment' in perm_name:
                perm = Permission.objects.get(
                    codename=perm_name,
                    content_type=equipment_ct
                )
            else:
                perm = Permission.objects.get(
                    codename=perm_name,
                    content_type=transfer_ct
                )
            
            normal_user_group.permissions.add(perm)

        self.stdout.write(
            self.style.SUCCESS('Pomyślnie skonfigurowano grupy użytkowników')
        )
        self.stdout.write(
            self.style.SUCCESS('Grupa IT: pełny dostęp do wszystkich funkcji')
        )
        self.stdout.write(
            self.style.SUCCESS('Grupa normal_user: tylko podgląd przypisanego sprzętu')
        ) 