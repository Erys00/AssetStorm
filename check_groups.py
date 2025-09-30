import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assetstorm.settings')
django.setup()

from django.contrib.auth.models import Group, Permission, User
from equipment.models import Equipment, EquipmentTransfer

print("=== SPRAWDZENIE GRUP I UPRAWNIEŃ ===")

# Sprawdź grupy
try:
    it_group = Group.objects.get(name='IT')
    print(f"\nGrupa IT: {it_group.name}")
    print(f"Liczba uprawnień: {it_group.permissions.count()}")
    print("Uprawnienia:")
    for perm in it_group.permissions.all():
        print(f"  - {perm.codename}: {perm.name}")
except Group.DoesNotExist:
    print("Grupa IT nie istnieje!")

try:
    normal_group = Group.objects.get(name='normal_user')
    print(f"\nGrupa normal_user: {normal_group.name}")
    print(f"Liczba uprawnień: {normal_group.permissions.count()}")
    print("Uprawnienia:")
    for perm in normal_group.permissions.all():
        print(f"  - {perm.codename}: {perm.name}")
except Group.DoesNotExist:
    print("Grupa normal_user nie istnieje!")

# Sprawdź użytkowników w grupach
print(f"\n=== UŻYTKOWNICY W GRUPACH ===")
it_users = User.objects.filter(groups__name='IT')
print(f"Użytkownicy w grupie IT: {it_users.count()}")
for user in it_users:
    print(f"  - {user.username} ({user.get_full_name()})")

normal_users = User.objects.filter(groups__name='normal_user')
print(f"Użytkownicy w grupie normal_user: {normal_users.count()}")
for user in normal_users:
    print(f"  - {user.username} ({user.get_full_name()})")

print(f"\n=== WSZYSCY UŻYTKOWNICY ===")
all_users = User.objects.all()
for user in all_users:
    groups = [g.name for g in user.groups.all()]
    groups_str = ", ".join(groups) if groups else "Brak grup"
    print(f"  - {user.username} ({user.get_full_name()}): {groups_str}")
