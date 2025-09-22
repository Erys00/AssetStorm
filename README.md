# AssetStorm - Ewidencja Sprzętu IT

Profesjonalna aplikacja webowa do zarządzania sprzętem IT dla małych i średnich firm, napisana w Django. System oferuje kompleksowe narzędzia do ewidencji, śledzenia i analizy sprzętu komputerowego.

## 🚀 Główne funkcjonalności

### 📊 Dashboard z analityką
- **Statystyki w czasie rzeczywistym** - liczba urządzeń według statusu
- **Analiza finansowa** - wartość sprzętu, średnie koszty (tylko dla IT)
- **Analiza według typów** - najpopularniejsze kategorie sprzętu
- **Analiza według dostawców** - najczęściej używane marki
- **Alerty gwarancyjne** - sprzęt z kończącą się gwarancją (30 dni)
- **Ostatnie transfery** - historia przekazań sprzętu
- **Monitoring serwisu** - sprzęt długo w naprawie

### 🔍 Zaawansowane wyszukiwanie i filtrowanie
- **Wyszukiwanie ogólne** - nazwa, numer seryjny, typ, numer faktury, lokalizacja, dostawca, uwagi
- **Filtry specjalistyczne** - status, lokalizacja, dostawca, użytkownik (IT)
- **Inteligentne dopasowania** - częściowe wyszukiwanie, ignorowanie wielkości liter
- **Kombinowane filtry** - możliwość łączenia wielu kryteriów

### 📋 Eksport i raportowanie
- **Eksport do Excel** - profesjonalne raporty z formatowaniem
- **Eksport sprzętu** - wszystkie dane w formacie .xlsx
- **Eksport transferów** - historia przekazań sprzętu
- **Automatyczne nazwy plików** - z datą i godziną generowania

### 📱 Kody QR
- **Automatyczne generowanie** - kody QR dla każdego sprzętu
- **Bezpośredni dostęp** - skanowanie prowadzi do szczegółów sprzętu
- **Pobieranie** - możliwość pobrania kodu QR jako obraz
- **Responsywny modal** - wyświetlanie w przeglądarce

### 🛠️ Harmonogram konserwacji
- **Planowanie przeglądów** - różne typy konserwacji
- **Śledzenie kosztów** - koszty napraw i techników
- **Status wykonania** - kontrola postępu prac
- **Historia konserwacji** - pełna dokumentacja

### 💰 Zarządzanie finansowe
- **Numer faktury** - śledzenie dokumentów zakupu
- **Cena zakupu** - wartość sprzętu
- **Dostawca** - firma dostarczająca sprzęt
- **Koniec gwarancji** - data wygaśnięcia gwarancji
- **Koszty konserwacji** - śledzenie wydatków na serwis

### 👥 Zarządzanie użytkownikami
- **Role użytkowników** - IT, zwykli użytkownicy
- **Kontrola dostępu** - różne uprawnienia według ról
- **Historia transferów** - śledzenie przekazań sprzętu
- **Przypisywanie sprzętu** - łatwe zarządzanie zasobami

## 📊 Statusy sprzętu

- **🟢 Dostępny** - sprzęt gotowy do użycia
- **🔵 W użyciu** - sprzęt aktualnie używany
- **🟡 Serwis** - sprzęt w naprawie
- **⚫ Wycofany** - sprzęt wycofany z użytku

## 🛠️ Instalacja i uruchomienie

### Wymagania systemowe

- Python 3.8+
- Django 5.2+
- SQLite (domyślnie) lub PostgreSQL/MySQL

### Krok 1: Klonowanie repozytorium

```bash
git clone <url-repozytorium>
cd AssetStorm
```

### Krok 2: Aktywacja środowiska wirtualnego

```bash
# Windows
myvenv\Scripts\activate

# Linux/Mac
source myvenv/bin/activate
```

### Krok 3: Instalacja zależności

```bash
pip install -r requirements.txt
```

### Krok 4: Migracje bazy danych

```bash
python manage.py makemigrations equipment
python manage.py migrate
```

### Krok 5: Tworzenie superużytkownika

```bash
python manage.py createsuperuser
```

### Krok 6: Uruchomienie serwera

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem: **http://127.0.0.1:8000/**

## 📖 Użytkowanie

### 🏠 Dashboard
- **Główna strona** - przegląd statystyk i alertów
- **Szybki dostęp** - do najważniejszych funkcji
- **Alerty** - gwarancje, serwis, transfery

### 📋 Zarządzanie sprzętem
1. **Lista sprzętu** - `/equipment/equipment/`
2. **Dodawanie sprzętu** - przycisk "Dodaj sprzęt"
3. **Szczegóły sprzętu** - kliknij na nazwę w liście
4. **Edycja** - przycisk "Edytuj" na stronie szczegółów
5. **Usuwanie** - przycisk "Usuń" na stronie szczegółów
6. **Transfer** - przycisk "Przekaż" do zmiany właściciela

### 🔍 Wyszukiwanie i filtrowanie
- **Pole wyszukiwania** - wpisz dowolny tekst
- **Filtr statusu** - wybierz status sprzętu
- **Filtr lokalizacji** - wyszukaj po lokalizacji
- **Filtr dostawcy** - znajdź sprzęt od konkretnej firmy
- **Filtr użytkownika** - tylko dla IT i adminów

### 📊 Eksport danych
- **Eksport Excel** - przycisk "Eksport Excel" na dashboard
- **Automatyczne pobieranie** - pliki .xlsx z datą i godziną
- **Formatowanie** - profesjonalne tabele z nagłówkami

### 📱 Kody QR
- **Generowanie** - przycisk "Kod QR" na stronie szczegółów
- **Skanowanie** - prowadzi bezpośrednio do szczegółów sprzętu
- **Pobieranie** - możliwość zapisania kodu jako obraz

## 🏗️ Struktura projektu

```
AssetStorm/
├── assetstorm/              # Główny projekt Django
│   ├── settings.py          # Ustawienia projektu
│   ├── urls.py              # Główny routing URL
│   └── ...
├── equipment/               # Aplikacja sprzętu
│   ├── models.py            # Modele Equipment, EquipmentTransfer, MaintenanceSchedule
│   ├── views.py             # Widoki aplikacji
│   ├── forms.py             # Formularze
│   ├── admin.py             # Konfiguracja panelu admina
│   ├── urls.py              # Routing URL aplikacji
│   ├── decorators.py        # Dekoratory kontroli dostępu
│   └── templates/           # Szablony HTML
│       └── equipment/
│           ├── base.html
│           ├── dashboard.html
│           ├── equipment_list.html
│           ├── equipment_detail.html
│           ├── equipment_form.html
│           ├── equipment_confirm_delete.html
│           ├── equipment_transfer.html
│           ├── my_equipment.html
│           └── login.html
├── media/                   # Pliki mediów (kody QR)
│   └── qr_codes/
├── manage.py                # Skrypt zarządzania Django
├── requirements.txt         # Zależności Python
└── README.md               # Ten plik
```

## 🛠️ Technologie

- **Backend**: Django 5.2.6
- **Baza danych**: SQLite (domyślnie)
- **Frontend**: HTML5, CSS3, Bootstrap 5, JavaScript
- **Ikony**: Font Awesome 6
- **Eksport**: openpyxl (Excel)
- **Kody QR**: qrcode + Pillow
- **Responsywność**: Bootstrap 5

## 📦 Zależności

```
asgiref==3.9.1
Django==5.2.6
sqlparse==0.5.3
openpyxl==3.1.5
qrcode[pil]==8.2
Pillow==11.3.0
```

## 🔧 Rozwój

### Dodawanie nowych funkcjonalności

1. Edytuj modele w `equipment/models.py`
2. Utwórz migracje: `python manage.py makemigrations`
3. Zastosuj migracje: `python manage.py migrate`
4. Dodaj widoki w `equipment/views.py`
5. Utwórz szablony w `equipment/templates/equipment/`
6. Zaktualizuj routing w `equipment/urls.py`

### Dostosowywanie wyglądu

Szablony używają Bootstrap 5. Możesz dostosować wygląd edytując:
- `equipment/templates/equipment/base.html` - główny szablon
- Poszczególne szablony w `equipment/templates/equipment/`

### Konfiguracja

- **Ustawienia**: `assetstorm/settings.py`
- **URL-e**: `assetstorm/urls.py`
- **Media**: `MEDIA_URL` i `MEDIA_ROOT`
- **Site URL**: `SITE_URL` dla kodów QR

## 🎯 Korzyści dla małych firm

### 💰 Oszczędności
- **Kontrola kosztów** - śledzenie wartości sprzętu
- **Planowanie budżetu** - alerty gwarancyjne
- **Optymalizacja** - analiza wykorzystania sprzętu

### ⏰ Efektywność
- **Szybkie wyszukiwanie** - zaawansowane filtry
- **Mobilny dostęp** - kody QR na telefonie
- **Automatyzacja** - eksport raportów

### 📊 Przejrzystość
- **Dashboard** - stan sprzętu na pierwszy rzut oka
- **Historia** - pełna dokumentacja transferów
- **Raporty** - dane dla księgowości

### 🛡️ Bezpieczeństwo
- **Kontrola dostępu** - role użytkowników
- **Audyt** - historia wszystkich zmian
- **Backup** - eksport danych

## 📞 Wsparcie

- **Dokumentacja**: Ten plik README
- **Panel admina**: `/admin/` - pełna administracja
- **Logi**: Sprawdzaj konsolę serwera Django

## 📄 Licencja

Ten projekt jest dostępny na licencji MIT.

## 👨‍💻 Autor

**AssetStorm** - Profesjonalny system ewidencji sprzętu IT dla małych i średnich firm.

---

*Ostatnia aktualizacja: Wrzesień 2025*