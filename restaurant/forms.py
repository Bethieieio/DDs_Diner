from .models import BookingModel, CreateReviews
from django import forms
from allauth.account.forms import SignupForm


class ClientSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self, request):

        user = super(ClientSignUpForm, self).save(request)
        return user

    class Meta:
        # model = User
        fields = ('email', ' first_name', 'last_name', 'password1', 'password2', )


class BookingForm(forms.ModelForm):
    class Meta:
        model = BookingModel
        fields = ('date', 'time', 'heads', 'allergies')
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'time': forms.DateInput(attrs={'type': 'time'}),
            'heads': forms.DateInput(attrs={'type': 'number'}),
            'allergies': forms.CheckboxInput,
        }


class ReviewForm(forms.ModelForm):
    class Meta:
        model = CreateReviews
        fields = ('review',)
