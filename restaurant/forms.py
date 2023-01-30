from .models import BookingModel
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ('date', 'time', 'heads')
        # date = forms.DateField()
        # time = forms.TimeField()
        # heads = forms.NumberInput()
        # allergies = forms.BooleanField()
