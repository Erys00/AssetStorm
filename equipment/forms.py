from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from .models import Equipment, EquipmentTransfer


class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = [
            'name', 'type', 'serial_number', 'invoice_number', 'purchase_date',
            'purchase_price', 'location', 'supplier', 'warranty_end_date',
            'status', 'assigned_to', 'notes'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'type': forms.TextInput(attrs={'class': 'form-control'}),
            'serial_number': forms.TextInput(attrs={'class': 'form-control'}),
            'invoice_number': forms.TextInput(attrs={'class': 'form-control'}),
            'purchase_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
            'purchase_price': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'supplier': forms.TextInput(attrs={'class': 'form-control'}),
            'warranty_end_date': forms.DateInput(
                attrs={'class': 'form-control', 'type': 'date'}
            ),
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
        self.fields['to_user'].required = True
        self.fields['reason'].label = 'Powód przekazania'
    
    def clean_to_user(self):
        to_user = self.cleaned_data.get('to_user')
        if not to_user:
            raise forms.ValidationError('Musisz wybrać użytkownika, do którego chcesz przekazać sprzęt.')
        return to_user


class CustomLoginForm(AuthenticationForm):
    """Niestandardowy formularz logowania z Bootstrap styling"""
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Nazwa użytkownika',
            'autofocus': True
        }),
        label='Nazwa użytkownika'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Hasło'
        }),
        label='Hasło'
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'form-control'})
        self.fields['password'].widget.attrs.update({'class': 'form-control'})


class EquipmentTransferApprovalForm(forms.Form):
    """Formularz do akceptacji/odrzucenia przekazania sprzętu"""
    ACTION_CHOICES = [
        ('approve', 'Zaakceptuj przekazanie'),
        ('reject', 'Odrzuć przekazanie'),
    ]
    
    action = forms.ChoiceField(
        choices=ACTION_CHOICES,
        widget=forms.RadioSelect(attrs={'class': 'form-check-input'}),
        label='Decyzja',
        required=True
    )
    
    reason = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Podaj powód odrzucenia (opcjonalne dla akceptacji)...'
            }
        ),
        label='Powód',
        required=False
    )
    
    def clean_reason(self):
        action = self.cleaned_data.get('action')
        reason = self.cleaned_data.get('reason')
        
        if action == 'reject' and not reason:
            raise forms.ValidationError('Powód odrzucenia jest wymagany.')
        
        return reason 