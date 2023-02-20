from .models import BookingModel, CreateReviews
from django import forms


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ('date', 'time', 'heads', 'allergies')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.TimeInput(attrs={'type': 'time'}),
            'heads': forms.DateInput(attrs={'type': 'number'}),
            'allergies': forms.CheckboxInput,
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CreateReviews
        fields = ('review',)
