from allauth.account.forms import SignupForm
from django import forms


class ClientSignUpForm(SignupForm):
    first_name = forms.CharField(max_length=30)
    last_name = forms.CharField(max_length=30)

    def save(self, request):

        user = super(ClientSignUpForm, self).save(request)
        return user

    class Meta:
        # model = User
        fields = (
            'email',
            'first_name',
            'last_name',
            'password1',
            'password2',
        )
