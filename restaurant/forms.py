from .models import BookingModel
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ('date', 'time', 'heads')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.DateInput(attrs={'type': 'time'}),
            'heads': forms.DateInput(attrs={'type': 'number'}),
        }
