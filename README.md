# AssetStorm - Ewidencja Sprzętu IT

Aplikacja webowa do prowadzenia ewidencji sprzętu IT dla małych firm, napisana w Django.

## Funkcjonalności

- **Zarządzanie sprzętem**: Dodawanie, edycja, usuwanie i przeglądanie sprzętu
- **Szczegółowe informacje**: Nazwa, typ, numer seryjny, data zakupu, lokalizacja, status
- **Przypisywanie użytkowników**: Możliwość przypisania sprzętu do konkretnych użytkowników
- **Filtrowanie i wyszukiwanie**: Wyszukiwanie po nazwie, numerze seryjnym, typie oraz filtrowanie po statusie
- **Panel administracyjny**: Pełny panel admina Django do zarządzania danymi
- **Responsywny design**: Interfejs dostosowany do urządzeń mobilnych

## Statusy sprzętu

- **Dostępny** - sprzęt gotowy do użycia
- **W użyciu** - sprzęt aktualnie używany
- **Serwis** - sprzęt w naprawie
- **Wycofany** - sprzęt wycofany z użytku

## Instalacja i uruchomienie

### Wymagania

- Python 3.8+
- Django 4.0+

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
pip install django
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

Aplikacja będzie dostępna pod adresem: http://127.0.0.1:8000/

## Użytkowanie

### Panel administracyjny

1. Przejdź do http://127.0.0.1:8000/admin/
2. Zaloguj się używając danych superużytkownika
3. W sekcji "Equipment" możesz zarządzać sprzętem

### Interfejs użytkownika

1. **Lista sprzętu** - główna strona z listą wszystkich sprzętów
2. **Dodawanie sprzętu** - przycisk "Dodaj sprzęt" w nawigacji
3. **Szczegóły sprzętu** - kliknij na nazwę sprzętu w liście
4. **Edycja** - przycisk "Edytuj" na stronie szczegółów
5. **Usuwanie** - przycisk "Usuń" na stronie szczegółów

### Filtrowanie i wyszukiwanie

- Użyj pola "Wyszukaj" do znalezienia sprzętu po nazwie, numerze seryjnym lub typie
- Użyj filtra "Status" do wyświetlenia sprzętu o określonym statusie
- Kliknij "Wyczyść" aby zresetować filtry

## Struktura projektu

```
AssetStorm/
├── assetstorm/          # Główny projekt Django
│   ├── settings.py      # Ustawienia projektu
│   ├── urls.py          # Główny routing URL
│   └── ...
├── equipment/           # Aplikacja sprzętu
│   ├── models.py        # Model Equipment
│   ├── views.py         # Widoki aplikacji
│   ├── forms.py         # Formularze
│   ├── admin.py         # Konfiguracja panelu admina
│   ├── urls.py          # Routing URL aplikacji
│   └── templates/       # Szablony HTML
│       └── equipment/
│           ├── base.html
│           ├── equipment_list.html
│           ├── equipment_detail.html
│           ├── equipment_form.html
│           └── equipment_confirm_delete.html
├── manage.py            # Skrypt zarządzania Django
└── README.md           # Ten plik
```

## Technologie

- **Backend**: Django 5.2
- **Baza danych**: SQLite (domyślnie)
- **Frontend**: HTML, CSS (Bootstrap 5), JavaScript
- **Ikony**: Font Awesome 6

## Rozwój

### Dodawanie nowych funkcjonalności

1. Edytuj model w `equipment/models.py`
2. Utwórz migracje: `python manage.py makemigrations`
3. Zastosuj migracje: `python manage.py migrate`
4. Dodaj widoki w `equipment/views.py`
5. Utwórz szablony w `equipment/templates/equipment/`
6. Zaktualizuj routing w `equipment/urls.py`

### Dostosowywanie wyglądu

Szablony używają Bootstrap 5. Możesz dostosować wygląd edytując:
- `equipment/templates/equipment/base.html` - główny szablon
- Poszczególne szablony w `equipment/templates/equipment/`

## Licencja

Ten projekt jest dostępny na licencji MIT.

## Autor

AssetStorm - System ewidencji sprzętu IT dla małych firm. 