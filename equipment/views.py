from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from django.utils import timezone
from .models import Equipment, EquipmentTransfer
from .forms import EquipmentForm, EquipmentTransferForm
from .decorators import it_staff_required, can_access_equipment, get_user_equipment_queryset, can_transfer_equipment


def equipment_list(request):
    """Lista wszystkich sprzętów z filtrowaniem i wyszukiwaniem"""
    # Użyj funkcji pomocniczej do filtrowania sprzętu
    equipment_list = get_user_equipment_queryset(request.user)
    
    # Wyszukiwanie
    search_query = request.GET.get('search', '')
    if search_query:
        equipment_list = equipment_list.filter(
            Q(name__icontains=search_query) |
            Q(serial_number__icontains=search_query) |
            Q(type__icontains=search_query)
        )
    
    # Filtrowanie po statusie
    status_filter = request.GET.get('status', '')
    if status_filter:
        equipment_list = equipment_list.filter(status=status_filter)
    
    # Filtrowanie po użytkowniku (tylko dla IT)
    user_filter = request.GET.get('user', '')
    if user_filter and (request.user.is_superuser or request.user.groups.filter(name='IT').exists()):
        equipment_list = equipment_list.filter(assigned_to__username=user_filter)
    
    # Paginacja
    paginator = Paginator(equipment_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'user_filter': user_filter,
        'status_choices': Equipment.STATUS_CHOICES,
        'is_it_staff': request.user.is_superuser or request.user.groups.filter(name='IT').exists(),
    }
    return render(request, 'equipment/equipment_list.html', context)


@login_required
@can_access_equipment
def equipment_detail(request, pk):
    """Szczegóły sprzętu"""
    equipment = get_object_or_404(Equipment, pk=pk)
    transfer_history = equipment.get_transfer_history()
    
    context = {
        'equipment': equipment,
        'transfer_history': transfer_history,
        'can_transfer': can_transfer_equipment(request.user, equipment),
        'is_it_staff': request.user.is_superuser or request.user.groups.filter(name='IT').exists(),
    }
    return render(request, 'equipment/equipment_detail.html', context)


@login_required
@it_staff_required
def equipment_create(request):
    """Dodawanie nowego sprzętu"""
    if request.method == 'POST':
        form = EquipmentForm(request.POST)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, f'Sprzęt "{equipment.name}" został dodany.')
            return redirect('equipment:equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm()
    
    return render(request, 'equipment/equipment_form.html', {'form': form, 'title': 'Dodaj sprzęt'})


@login_required
@can_access_equipment
def equipment_update(request, pk):
    """Edycja sprzętu"""
    equipment = get_object_or_404(Equipment, pk=pk)
    
    # Sprawdź czy użytkownik może edytować sprzęt
    if not (request.user.is_superuser or request.user.groups.filter(name='IT').exists()):
        if equipment.assigned_to != request.user:
            messages.error(request, 'Nie możesz edytować tego sprzętu.')
            return redirect('equipment:my_equipment')
    
    if request.method == 'POST':
        form = EquipmentForm(request.POST, instance=equipment)
        if form.is_valid():
            equipment = form.save()
            messages.success(request, f'Sprzęt "{equipment.name}" został zaktualizowany.')
            return redirect('equipment:equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentForm(instance=equipment)
    
    return render(request, 'equipment/equipment_form.html', {
        'form': form, 
        'equipment': equipment,
        'title': 'Edytuj sprzęt'
    })


@login_required
@it_staff_required
def equipment_delete(request, pk):
    """Usuwanie sprzętu"""
    equipment = get_object_or_404(Equipment, pk=pk)
    if request.method == 'POST':
        equipment_name = equipment.name
        equipment.delete()
        messages.success(request, f'Sprzęt "{equipment_name}" został usunięty.')
        return redirect('equipment:equipment_list')
    
    return render(request, 'equipment/equipment_confirm_delete.html', {'equipment': equipment})


@login_required
@can_access_equipment
def equipment_transfer(request, pk):
    """Przekazywanie sprzętu innemu użytkownikowi"""
    equipment = get_object_or_404(Equipment, pk=pk)
    
    # Sprawdź czy użytkownik może przekazać sprzęt
    if not can_transfer_equipment(request.user, equipment):
        messages.error(request, 'Nie możesz przekazać tego sprzętu.')
        return redirect('equipment:equipment_detail', pk=equipment.pk)
    
    if request.method == 'POST':
        form = EquipmentTransferForm(request.POST)
        if form.is_valid():
            transfer = form.save(commit=False)
            transfer.equipment = equipment
            transfer.from_user = equipment.assigned_to
            transfer.transferred_by = request.user
            
            # Aktualizuj przypisanie sprzętu
            equipment.assigned_to = transfer.to_user
            equipment.status = 'in_use'
            equipment.save()
            
            # Zapisz transfer
            transfer.save()
            
            messages.success(
                request, 
                f'Sprzęt "{equipment.name}" został przekazany użytkownikowi '
                f'{transfer.to_user.get_full_name() or transfer.to_user.username}.'
            )
            return redirect('equipment:equipment_detail', pk=equipment.pk)
    else:
        form = EquipmentTransferForm()
    
    context = {
        'form': form,
        'equipment': equipment,
        'title': f'Przekaż sprzęt: {equipment.name}'
    }
    return render(request, 'equipment/equipment_transfer.html', context)


@login_required
def my_equipment(request):
    """Lista sprzętu przypisanego do zalogowanego użytkownika"""
    equipment_list = get_user_equipment_queryset(request.user)
    
    # Wyszukiwanie
    search_query = request.GET.get('search', '')
    if search_query:
        equipment_list = equipment_list.filter(
            Q(name__icontains=search_query) |
            Q(serial_number__icontains=search_query) |
            Q(type__icontains=search_query)
        )
    
    # Filtrowanie po statusie
    status_filter = request.GET.get('status', '')
    if status_filter:
        equipment_list = equipment_list.filter(status=status_filter)
    
    # Paginacja
    paginator = Paginator(equipment_list, 20)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj,
        'search_query': search_query,
        'status_filter': status_filter,
        'status_choices': Equipment.STATUS_CHOICES,
        'is_it_staff': request.user.is_superuser or request.user.groups.filter(name='IT').exists(),
    }
    return render(request, 'equipment/my_equipment.html', context)
