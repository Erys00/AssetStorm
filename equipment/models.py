from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class Equipment(models.Model):
    STATUS_CHOICES = [
        ('available', 'Dostępny'),
        ('in_use', 'W użyciu'),
        ('service', 'Serwis'),
        ('retired', 'Wycofany'),
    ]

    name = models.CharField('Nazwa', max_length=100)
    type = models.CharField('Typ', max_length=100)
    serial_number = models.CharField(
        'Numer seryjny', max_length=100, unique=True
    )
    invoice_number = models.CharField(
        'Numer faktury', max_length=100, blank=True, null=True
    )
    purchase_date = models.DateField('Data zakupu')
    purchase_price = models.DecimalField(
        'Cena zakupu', max_digits=10, decimal_places=2, blank=True, null=True
    )
    location = models.CharField('Lokalizacja', max_length=100)
    supplier = models.CharField('Dostawca', max_length=100, blank=True)
    warranty_end_date = models.DateField('Koniec gwarancji', blank=True, null=True)
    status = models.CharField(
        'Status', max_length=20, choices=STATUS_CHOICES, default='available'
    )
    assigned_to = models.ForeignKey(
        User,
        verbose_name='Przypisany użytkownik',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='assigned_equipment'
    )
    notes = models.TextField('Uwagi', blank=True)
    created_at = models.DateTimeField('Data utworzenia', auto_now_add=True)
    updated_at = models.DateTimeField('Data aktualizacji', auto_now=True)

    class Meta:
        verbose_name = 'Sprzęt'
        verbose_name_plural = 'Sprzęt'
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.name} ({self.serial_number})"
    
    def get_status_display_class(self):
        """Zwraca klasę CSS dla statusu"""
        status_classes = {
            'available': 'success',
            'in_use': 'primary',
            'service': 'warning',
            'retired': 'secondary',
        }
        return status_classes.get(self.status, 'secondary')
    
    def can_be_transferred(self):
        """Sprawdza czy sprzęt może być przekazany"""
        return self.status in ['available', 'in_use']
    
    def get_transfer_history(self):
        """Zwraca historię przekazań sprzętu"""
        return self.transfers.all().order_by('-transfer_date')


class EquipmentTransfer(models.Model):
    """Model do śledzenia historii przekazań sprzętu"""
    equipment = models.ForeignKey(
        Equipment,
        on_delete=models.CASCADE,
        related_name='transfers',
        verbose_name='Sprzęt'
    )
    from_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transfers_from',
        verbose_name='Od użytkownika'
    )
    to_user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='transfers_to',
        verbose_name='Do użytkownika'
    )
    transfer_date = models.DateTimeField('Data przekazania', default=timezone.now)
    reason = models.TextField('Powód przekazania', blank=True)
    transferred_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='transfers_created',
        verbose_name='Przekazane przez'
    )
    
    class Meta:
        verbose_name = 'Przekazanie sprzętu'
        verbose_name_plural = 'Przekazania sprzętu'
        ordering = ['-transfer_date']
    
    def __str__(self):
        from_user = (self.from_user.get_full_name()
                     if self.from_user else "System")
        to_user = (self.to_user.get_full_name()
                   if self.to_user else "System")
        return f"{self.equipment.name} - od {from_user} do {to_user}"


class MaintenanceSchedule(models.Model):
    """Model do zarządzania harmonogramem konserwacji sprzętu"""
    MAINTENANCE_TYPES = [
        ('preventive', 'Przegląd prewencyjny'),
        ('repair', 'Naprawa'),
        ('cleaning', 'Czyszczenie'),
        ('update', 'Aktualizacja'),
        ('inspection', 'Kontrola'),
    ]
    
    equipment = models.ForeignKey(
        Equipment, on_delete=models.CASCADE, verbose_name='Sprzęt'
    )
    maintenance_type = models.CharField(
        'Typ konserwacji', max_length=20, choices=MAINTENANCE_TYPES
    )
    scheduled_date = models.DateField('Zaplanowana data')
    completed_date = models.DateField('Data wykonania', blank=True, null=True)
    description = models.TextField('Opis konserwacji')
    cost = models.DecimalField(
        'Koszt', max_digits=10, decimal_places=2, blank=True, null=True
    )
    technician = models.CharField('Technik', max_length=100, blank=True)
    notes = models.TextField('Uwagi', blank=True)
    is_completed = models.BooleanField('Wykonane', default=False)
    created_at = models.DateTimeField('Data utworzenia', auto_now_add=True)
    updated_at = models.DateTimeField('Data aktualizacji', auto_now=True)

    class Meta:
        verbose_name = 'Harmonogram konserwacji'
        verbose_name_plural = 'Harmonogramy konserwacji'
        ordering = ['scheduled_date']

    def __str__(self):
        status = "✓" if self.is_completed else "⏳"
        return f'{status} {self.equipment.name} - {self.get_maintenance_type_display()} ({self.scheduled_date})'
