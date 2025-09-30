import os
import django

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'assetstorm.settings')
django.setup()

from django.contrib.auth.models import Group, User

print("=== PRZYPISYWANIE UŻYTKOWNIKÓW DO GRUP ===")

# Pobierz grupy
try:
    it_group = Group.objects.get(name='IT')
    normal_group = Group.objects.get(name='normal_user')
except Group.DoesNotExist as e:
    print(f"Błąd: {e}")
    exit()

# Przypisz superusera (admin) do grupy IT
try:
    admin_user = User.objects.get(username='admin')
    admin_user.groups.add(it_group)
    print(f"[OK] Przypisano admina do grupy IT")
except User.DoesNotExist:
    print("Nie znaleziono użytkownika admin")

# Przypisz użytkownika ewilk do grupy IT
try:
    ewilk_user = User.objects.get(username='ewilk')
    ewilk_user.groups.add(it_group)
    print(f"[OK] Przypisano ewilk do grupy IT")
except User.DoesNotExist:
    print("Nie znaleziono użytkownika ewilk")

# Przypisz kilku losowych użytkowników do grupy IT (jako przykłady)
it_users = [
    'karolina.kozłowski',
    'marek.pietrzak', 
    'michał.wilk',
    'eryk.król',
    'rafał.stępień'
]

for username in it_users:
    try:
        user = User.objects.get(username=username)
        user.groups.add(it_group)
        print(f"[OK] Przypisano {username} do grupy IT")
    except User.DoesNotExist:
        print(f"Nie znaleziono użytkownika {username}")

# Przypisz pozostałych użytkowników do grupy normal_user
all_users = User.objects.exclude(groups__name='IT')  # Wyklucz użytkowników IT
normal_count = 0
for user in all_users:
    user.groups.add(normal_group)
    normal_count += 1

print(f"[OK] Przypisano {normal_count} użytkowników do grupy normal_user")

# Podsumowanie
print(f"\n=== PODSUMOWANIE ===")
it_count = User.objects.filter(groups__name='IT').count()
normal_count = User.objects.filter(groups__name='normal_user').count()

print(f"Użytkownicy w grupie IT: {it_count}")
it_users = User.objects.filter(groups__name='IT')
for user in it_users:
    print(f"  - {user.username} ({user.get_full_name()})")

print(f"\nUżytkownicy w grupie normal_user: {normal_count}")

print(f"\n✓ Konfiguracja grup zakończona pomyślnie!")
