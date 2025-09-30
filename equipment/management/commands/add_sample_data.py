from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from equipment.models import Equipment
from datetime import date, timedelta
from decimal import Decimal
import random

def create_equipment_data():
    """Tworzy 120 sprzętów różnych typów"""
    
    # Lista prawdziwych nazw sprzętów
    computers = [
        "Dell OptiPlex 3060",
        "Dell OptiPlex 3070", 
        "Dell OptiPlex 3080",
        "Dell OptiPlex 3090",
        "Dell OptiPlex 7090",
        "HP EliteDesk 800 G6",
        "HP EliteDesk 800 G7",
        "HP ProDesk 400 G6",
        "HP ProDesk 400 G7",
        "Lenovo ThinkCentre M720",
        "Lenovo ThinkCentre M920",
        "Lenovo ThinkCentre M930",
        "ASUS ExpertCenter D7",
        "ASUS ExpertCenter D5",
        "Acer Veriton N4660G",
        "Acer Veriton N4660G",
    ]
    
    laptops = [
        "ASUS ExpertBook B9",
        "ASUS ExpertBook B7",
        "ASUS VivoBook S15",
        "Dell Latitude 5420",
        "Dell Latitude 5520",
        "Dell Latitude 7420",
        "Dell Latitude 7520",
        "HP EliteBook 840 G8",
        "HP EliteBook 850 G8",
        "HP ProBook 450 G8",
        "HP ProBook 470 G8",
        "Lenovo ThinkPad E14",
        "Lenovo ThinkPad E15",
        "Lenovo ThinkPad T14",
        "Lenovo ThinkPad T15",
        "Lenovo ThinkPad X1 Carbon",
        "Acer TravelMate P2",
        "Acer TravelMate P6",
        "Acer Swift 3",
        "Acer Aspire 5",
    ]
    
    monitors = [
        "Dell UltraSharp U2720Q",
        "Dell UltraSharp U2720D",
        "Dell UltraSharp U2422H",
        "Dell UltraSharp U2422HE",
        "Dell P2419H",
        "Dell P2720D",
        "HP EliteDisplay E243",
        "HP EliteDisplay E273q",
        "HP EliteDisplay E244c",
        "HP Z27n G2",
        "Lenovo ThinkVision T24i-20",
        "Lenovo ThinkVision T27i-20",
        "Lenovo ThinkVision P27h-20",
        "ASUS ProArt PA248QV",
        "ASUS ProArt PA278QV",
        "ASUS VG248QE",
        "ASUS VG279Q",
        "Acer Nitro VG240Y",
        "Acer Predator XB271HU",
        "Acer CB242Y",
    ]
    
    phones = [
        "Samsung Galaxy S21",
        "Samsung Galaxy S22",
        "Samsung Galaxy S23",
        "Samsung Galaxy A52",
        "Samsung Galaxy A53",
        "Samsung Galaxy A73",
        "iPhone 12",
        "iPhone 13",
        "iPhone 14",
        "iPhone 15",
        "iPhone SE (3rd gen)",
        "Google Pixel 6",
        "Google Pixel 7",
        "Google Pixel 8",
        "OnePlus 9",
        "OnePlus 10",
        "OnePlus 11",
        "Xiaomi Mi 11",
        "Xiaomi Mi 12",
        "Xiaomi Redmi Note 11",
        "Huawei P50",
        "Huawei P60",
        "Motorola Edge 30",
        "Motorola Edge 40",
        "Sony Xperia 1 III",
        "Sony Xperia 5 III",
    ]
    
    # Statusy sprzętu
    statuses = ['available', 'in_use', 'service', 'retired']
    status_weights = [40, 45, 10, 5]  # Większość sprzętu w użyciu lub dostępna
    
    # Lokalizacje
    locations = [
        "Biuro - Warszawa",
        "Biuro - Kraków", 
        "Biuro - Gdańsk",
        "Biuro - Wrocław",
        "Biuro - Poznań",
        "Magazyn główny",
        "Siedziba centrala",
        "Oddział południe",
        "Oddział północ",
        "Serwis zewnętrzny"
    ]
    
    # Dostawcy
    suppliers = [
        "Dell Technologies",
        "HP Inc.",
        "Lenovo",
        "ASUS",
        "Acer",
        "Samsung",
        "Apple",
        "Google",
        "OnePlus",
        "Xiaomi",
        "Huawei",
        "Motorola",
        "Sony",
        "Komputronik",
        "Morele.net",
        "X-kom",
        "Media Expert"
    ]
    
    equipment_list = []
    
    # Generuj sprzęt
    serial_counter = 1001
    
    # 30 komputerów
    for i in range(30):
        name = random.choice(computers)
        serial_number = f"PC-{serial_counter:04d}"
        serial_counter += 1
        
        purchase_date = date.today() - timedelta(days=random.randint(30, 1000))
        warranty_end_date = purchase_date + timedelta(days=1095)  # 3 lata gwarancji
        
        equipment_list.append({
            'name': name,
            'type': 'Komputer stacjonarny',
            'serial_number': serial_number,
            'invoice_number': f"FV/2023/{random.randint(1000, 9999)}",
            'purchase_date': purchase_date,
            'purchase_price': Decimal(str(random.randint(2000, 8000))),
            'location': random.choice(locations),
            'supplier': random.choice(suppliers),
            'warranty_end_date': warranty_end_date,
            'status': random.choices(statuses, weights=status_weights)[0],
            'notes': f"Komputer biurowy - {name}"
        })
    
    # 25 laptopów
    for i in range(25):
        name = random.choice(laptops)
        serial_number = f"LT-{serial_counter:04d}"
        serial_counter += 1
        
        purchase_date = date.today() - timedelta(days=random.randint(30, 800))
        warranty_end_date = purchase_date + timedelta(days=1095)
        
        equipment_list.append({
            'name': name,
            'type': 'Laptop',
            'serial_number': serial_number,
            'invoice_number': f"FV/2023/{random.randint(1000, 9999)}",
            'purchase_date': purchase_date,
            'purchase_price': Decimal(str(random.randint(3000, 12000))),
            'location': random.choice(locations),
            'supplier': random.choice(suppliers),
            'warranty_end_date': warranty_end_date,
            'status': random.choices(statuses, weights=status_weights)[0],
            'notes': f"Laptop służbowy - {name}"
        })
    
    # 35 monitorów
    for i in range(35):
        name = random.choice(monitors)
        serial_number = f"MN-{serial_counter:04d}"
        serial_counter += 1
        
        purchase_date = date.today() - timedelta(days=random.randint(30, 600))
        warranty_end_date = purchase_date + timedelta(days=1095)
        
        equipment_list.append({
            'name': name,
            'type': 'Monitor',
            'serial_number': serial_number,
            'invoice_number': f"FV/2023/{random.randint(1000, 9999)}",
            'purchase_date': purchase_date,
            'purchase_price': Decimal(str(random.randint(800, 3000))),
            'location': random.choice(locations),
            'supplier': random.choice(suppliers),
            'warranty_end_date': warranty_end_date,
            'status': random.choices(statuses, weights=status_weights)[0],
            'notes': f"Monitor - {name}"
        })
    
    # 30 telefonów
    for i in range(30):
        name = random.choice(phones)
        serial_number = f"PH-{serial_counter:04d}"
        serial_counter += 1
        
        purchase_date = date.today() - timedelta(days=random.randint(30, 400))
        warranty_end_date = purchase_date + timedelta(days=730)  # 2 lata gwarancji dla telefonów
        
        equipment_list.append({
            'name': name,
            'type': 'Telefon komórkowy',
            'serial_number': serial_number,
            'invoice_number': f"FV/2023/{random.randint(1000, 9999)}",
            'purchase_date': purchase_date,
            'purchase_price': Decimal(str(random.randint(1500, 6000))),
            'location': random.choice(locations),
            'supplier': random.choice(suppliers),
            'warranty_end_date': warranty_end_date,
            'status': random.choices(statuses, weights=status_weights)[0],
            'notes': f"Telefon służbowy - {name}"
        })
    
    return equipment_list

def create_users_data():
    """Tworzy 50 użytkowników"""
    
    # Polskie imiona i nazwiska
    first_names = [
        "Adam", "Adrian", "Agnieszka", "Aleksander", "Alicja", "Anna", "Bartosz", "Beata",
        "Dariusz", "Dorota", "Eryk", "Ewa", "Filip", "Grzegorz", "Iwona", "Jakub",
        "Jan", "Joanna", "Kamil", "Karolina", "Krzysztof", "Łukasz", "Magdalena", "Marcin",
        "Marek", "Mariusz", "Michał", "Monika", "Paweł", "Piotr", "Rafał", "Renata",
        "Robert", "Sebastian", "Sylwia", "Tomasz", "Urszula", "Wojciech", "Zbigniew", "Żaneta"
    ]
    
    last_names = [
        "Wilk", "Nowak", "Kowalski", "Wiśniewski", "Dąbrowski", "Lewandowski", "Wójcik",
        "Kamiński", "Kowalczyk", "Zieliński", "Szymański", "Woźniak", "Kozłowski", "Jankowski",
        "Mazur", "Kwiatkowski", "Krawczyk", "Piotrowski", "Grabowski", "Nowakowski", "Pawłowski",
        "Michalski", "Król", "Nowicki", "Wieczorek", "Wróbel", "Jabłoński", "Majewski",
        "Olszewski", "Stępień", "Malinowski", "Jaworski", "Adamczyk", "Dudek", "Pietrzak"
    ]
    
    departments = [
        "IT", "HR", "Finanse", "Marketing", "Sprzedaż", "Obsługa klienta", "Produkcja",
        "Logistyka", "Kontrola jakości", "Badania i rozwój", "Prawo", "Zarządzanie"
    ]
    
    users_list = []
    
    for i in range(50):
        first_name = random.choice(first_names)
        last_name = random.choice(last_names)
        email = f"{first_name.lower()}.{last_name.lower()}@asset-test.pl"
        
        # Upewnij się, że email jest unikalny
        counter = 1
        original_email = email
        while email in [user['email'] for user in users_list]:
            email = f"{first_name.lower()}.{last_name.lower()}{counter}@asset-test.pl"
            counter += 1
        
        users_list.append({
            'username': email.split('@')[0],
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'department': random.choice(departments)
        })
    
    return users_list

class Command(BaseCommand):
    help = 'Dodaje przykładowe dane do bazy - 120 sprzętów i 50 użytkowników'

    def handle(self, *args, **options):
        self.stdout.write("Dodawanie przykładowych danych do bazy...")
        
        # Tworzenie użytkowników
        self.stdout.write("Tworzenie 50 użytkowników...")
        users_data = create_users_data()
        created_users = []
        
        for user_data in users_data:
            try:
                user = User.objects.create_user(
                    username=user_data['username'],
                    email=user_data['email'],
                    password='password123',  # Standardowe hasło dla wszystkich
                    first_name=user_data['first_name'],
                    last_name=user_data['last_name']
                )
                created_users.append(user)
                self.stdout.write(f"Utworzono użytkownika: {user.get_full_name()} ({user.email})")
            except Exception as e:
                self.stdout.write(f"Błąd przy tworzeniu użytkownika {user_data['username']}: {e}")
        
        self.stdout.write(f"Utworzono {len(created_users)} użytkowników")
        
        # Tworzenie sprzętu
        self.stdout.write("\nTworzenie 120 sprzętów...")
        equipment_data = create_equipment_data()
        created_equipment = []
        
        for eq_data in equipment_data:
            try:
                # Losowo przypisz użytkownika do sprzętu w statusie "in_use"
                assigned_user = None
                if eq_data['status'] == 'in_use' and created_users:
                    assigned_user = random.choice(created_users)
                
                equipment = Equipment.objects.create(
                    name=eq_data['name'],
                    type=eq_data['type'],
                    serial_number=eq_data['serial_number'],
                    invoice_number=eq_data['invoice_number'],
                    purchase_date=eq_data['purchase_date'],
                    purchase_price=eq_data['purchase_price'],
                    location=eq_data['location'],
                    supplier=eq_data['supplier'],
                    warranty_end_date=eq_data['warranty_end_date'],
                    status=eq_data['status'],
                    assigned_to=assigned_user,
                    notes=eq_data['notes']
                )
                
                # Generuj kod QR
                equipment.generate_qr_code()
                created_equipment.append(equipment)
                self.stdout.write(f"Utworzono sprzęt: {equipment.name} ({equipment.serial_number})")
                
            except Exception as e:
                self.stdout.write(f"Błąd przy tworzeniu sprzętu {eq_data['name']}: {e}")
        
        self.stdout.write(f"\nUtworzono {len(created_equipment)} sprzętów")
        self.stdout.write(self.style.SUCCESS("\nPrzykładowe dane zostały pomyślnie dodane do bazy!"))
