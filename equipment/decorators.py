from functools import wraps
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import Group


def it_staff_required(view_func):
    """
    Dekorator sprawdzający czy użytkownik należy do grupy IT
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Sprawdź czy użytkownik jest w grupie IT lub jest superuser
            if request.user.is_superuser or request.user.groups.filter(name='IT').exists():
                return view_func(request, *args, **kwargs)
            else:
                messages.error(request, 'Nie masz uprawnień do wykonania tej operacji.')
                return redirect('equipment:my_equipment')
        else:
            return redirect('equipment:login')
    return _wrapped_view


def can_access_equipment(view_func):
    """
    Dekorator sprawdzający czy użytkownik może uzyskać dostęp do konkretnego sprzętu
    """
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if request.user.is_authenticated:
            # Superuser i IT mają pełny dostęp
            if request.user.is_superuser or request.user.groups.filter(name='IT').exists():
                return view_func(request, *args, **kwargs)
            
            # Sprawdź czy użytkownik ma dostęp do konkretnego sprzętu
            equipment_id = kwargs.get('pk')
            if equipment_id:
                from .models import Equipment
                try:
                    equipment = Equipment.objects.get(pk=equipment_id)
                    if equipment.assigned_to == request.user:
                        return view_func(request, *args, **kwargs)
                    else:
                        messages.error(request, 'Nie masz dostępu do tego sprzętu.')
                        return redirect('equipment:my_equipment')
                except Equipment.DoesNotExist:
                    messages.error(request, 'Sprzęt nie istnieje.')
                    return redirect('equipment:my_equipment')
            
            return view_func(request, *args, **kwargs)
        else:
            return redirect('equipment:login')
    return _wrapped_view


def get_user_equipment_queryset(user):
    """
    Funkcja pomocnicza zwracająca queryset sprzętu dostępnego dla użytkownika
    """
    from .models import Equipment
    
    # Sprawdź czy użytkownik jest zalogowany
    if not user.is_authenticated:
        return Equipment.objects.none()
    
    if user.is_superuser or user.groups.filter(name='IT').exists():
        # Pełny dostęp dla superuser i IT
        return Equipment.objects.all()
    else:
        # Tylko przypisany sprzęt dla normalnych użytkowników
        return Equipment.objects.filter(assigned_to=user)


def can_transfer_equipment(user, equipment):
    """
    Sprawdza czy użytkownik może przekazać konkretny sprzęt
    """
    if user.is_superuser or user.groups.filter(name='IT').exists():
        return equipment.can_be_transferred()
    else:
        # Normalny użytkownik może przekazać tylko swój sprzęt
        return equipment.assigned_to == user and equipment.can_be_transferred() 