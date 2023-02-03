from django.shortcuts import render
from django.views import View
from .forms import BookingForm, ClientSignUpForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

# Create your views here.


class Home(View):
    def get(self, request):
        signupform = ClientSignUpForm()

        return render(
            request,
            "index.html",
            {
                "signupform": signupform,
            }
        )


class Menu(View):
    def get(self, request):

        return render(
            request,
            "menu.html",
        )


class Reviews(View):
    def get(self, request):

        return render(
            request,
            "reviews.html",
        )


@method_decorator(login_required, name='dispatch')
class BookingCreation(View):
    def get(self, request):

        return render(
            request,
            "booking_creation.html",
            {
                "booking_form": BookingForm(),
            }
        )

    def post(self, request):
        booking_form = BookingForm(data=request.POST)
        if booking_form.is_valid():
            booking.user = request.user
            booking = booking_form.save(commit=False)
            booking.save()
        else:
            booking_form = BookingForm()

        print('booking form')
        print(booking_form)
        return render(
            request,
            "booking_creation.html",
            {
                "booking_form": booking_form,
            }
        )


class ClientAdmin(View):
    def get(self, request):

        return render(
            request,
            "client_admin.html",
        )
