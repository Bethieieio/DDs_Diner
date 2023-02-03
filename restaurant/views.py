from django.shortcuts import render
from django.views import generic, View
from .forms import BookingForm, ClientSignUpForm

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
            # TODO ADD AUTHENTICATED USER TO BOOKING MODEL using @login_required
            # booking.user = request.user
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
