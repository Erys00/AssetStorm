from django import forms
from django.contrib.auth.models import User
from .models import Equipment, EquipmentTransfer


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'name', 'type', 'serial_number', 'purchase_date',
            'location', 'status', 'assigned_to', 'notes'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'assigned_to': forms.Select(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3}
            ),
        }


class EquipmentTransferForm(forms.ModelForm):
    class Meta:
        model = EquipmentTransfer
        fields = ['to_user', 'reason']
        widgets = {
            'to_user': forms.Select(attrs={'class': 'form-control'}),
            'reason': forms.Textarea(
                attrs={'class': 'form-control', 'rows': 3, 
                       'placeholder': 'Podaj powód przekazania sprzętu...'}
            ),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filtrujemy tylko aktywnych użytkowników
        self.fields['to_user'].queryset = User.objects.filter(is_active=True)
        self.fields['to_user'].label = 'Przekaż do użytkownika'
        self.fields['reason'].label = 'Powód przekazania' 