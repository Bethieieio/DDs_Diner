from django.shortcuts import render
from django.views import View
from .forms import BookingForm, ClientSignUpForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import BookingModel, CreateReviews
from django.http import HttpResponseRedirect
from django.contrib import messages

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
        review_form = ReviewForm()
        reviews = CreateReviews.objects.all()

        return render(
            request,
            "reviews.html",
            {
                "review_form": review_form,
                "reviews": reviews,
            }
        )

    # TODO add add login decorator here and thats for stopping people creating reviews if they are not logged in
    def post(self, request):
        review_form = ReviewForm(data=request.POST)
        if review_form.is_valid():
            review = review_form.save(commit=False)
            review.user = request.user
            review.save()
            messages.success(request, 'Thank You! Your review has been submitted!')

            return HttpResponseRedirect('/reviews')
        return render(
            request,
            "reviews.html",
            {
                "review_form": review_form,
            }
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
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            
            return HttpResponseRedirect('/your_bookings')
        else:
            booking_form = BookingForm()

        return render(
            request,
            "booking_creation.html",
            {
                "booking_form": booking_form,
            }
        )


@method_decorator(login_required, name='dispatch')
class ClientAdmin(View):
    def get(self, request):
        bookings = BookingModel.objects.filter(user_id=request.user.id)
        return render(
            request,
            "client_admin.html",
            {
                "bookings": bookings
            }
        )


