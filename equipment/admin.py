from django.contrib import admin
from .models import Equipment, EquipmentTransfer


@admin.register(Equipment)
class EquipmentAdmin(admin.ModelAdmin):
    list_display = [
        'name', 'type', 'serial_number', 'status', 
        'assigned_to', 'location', 'purchase_date'
    ]
    list_filter = ['status', 'type', 'location', 'purchase_date']
    search_fields = ['name', 'serial_number', 'type']
    list_editable = ['status', 'assigned_to']
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Podstawowe informacje', {
            'fields': ('name', 'type', 'serial_number', 'purchase_date')
        }),
        ('Lokalizacja i status', {
            'fields': ('location', 'status', 'assigned_to')
        }),
        ('Dodatkowe informacje', {
            'fields': ('notes', 'created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )


@admin.register(EquipmentTransfer)
class EquipmentTransferAdmin(admin.ModelAdmin):
    list_display = ['equipment', 'from_user', 'to_user', 'transfer_date', 'transferred_by']
    list_filter = ['transfer_date', 'equipment', 'from_user', 'to_user', 'transferred_by']
    search_fields = ['equipment__name', 'equipment__serial_number', 'from_user__username', 'to_user__username']
    readonly_fields = ['transfer_date']
    list_per_page = 25
    
    fieldsets = (
        ('Informacje o transferze', {
            'fields': ('equipment', 'from_user', 'to_user', 'transfer_date')
        }),
        ('Szczegóły', {
            'fields': ('reason', 'transferred_by')
        }),
    )
