from django import forms
from .models import Parcel, StatusUpdate

class ParcelForm(forms.ModelForm):
    class Meta:
        model = Parcel
        fields = ['sender_name', 'receiver_name', 'receiver_address', 'weight', 'status']
        widgets = {
            'sender_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Sender Name'}),
            'receiver_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Receiver Name'}),
            'receiver_address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Receiver Address'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Weight (kg)'}),
            'status': forms.Select(attrs={'class': 'form-select'}),
        }

class StatusUpdateForm(forms.ModelForm):
    class Meta:
        model = StatusUpdate
        fields = ['parcel', 'status', 'location']
