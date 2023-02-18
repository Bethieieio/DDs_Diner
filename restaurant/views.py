from django.shortcuts import render, get_object_or_404
from django.views import View
from .forms import BookingForm, ClientSignUpForm, ReviewForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import BookingModel, CreateReviews, CreateReviews, LikeReviews
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.core.exceptions import PermissionDenied

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

        if (request.user):
            userLikes = LikeReviews.objects.filter(user__id=request.user.id)
        else:
            userLikes = []
        # count all review likes?

        return render(
            request,
            "reviews.html",
            {
                "review_form": review_form,
                "reviews": reviews,
                "userLikes": userLikes.values_list('review__id', flat=True),
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
    # TODO booking availability validation 
    # make new method for ajax call to validate table availability 
    # user selects date and time and heads
    # make ajax call to check availability 
    # fetch bookings within time frame (booking date and time + 1 hour)
    # run algorithm to asercertain if fully booked for that table size
    # return bolean for front end
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
class BookingEdit(View):
    def get(self, request, id):
        booking = get_object_or_404(BookingModel, id=id)

        if (request.user.id != booking.user.id):
            raise PermissionDenied()
        return render(
            request,
            "booking_edit.html",
            {
                'booking_form': BookingForm(instance=booking),
                'booking': booking
            }
        )
    def post(self, request, id):
        booking = get_object_or_404(BookingModel, id=id)

        if (request.user.id != booking.user.id):
            raise PermissionDenied()
        booking_form = BookingForm(instance=booking, data=request.POST)
        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.save()
            
            return HttpResponseRedirect('/your_bookings')
        else:
            booking_form = BookingForm()
        return render(
            request,
            "booking_edit.html",
            {
                'booking_form': BookingForm(instance=booking),
                'booking': booking
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


@method_decorator(login_required, name='dispatch')
class BookingDelete(View):
    def post(self, request, id):
        booking = get_object_or_404(BookingModel, id=id)
        if (request.user.id != booking.user.id):
            raise PermissionDenied()
            
        booking.delete()
        return HttpResponseRedirect('/your_bookings')


@method_decorator(login_required, name='dispatch')
class LikeReview(View):
    def post(self, request, reviewId):
        review = get_object_or_404(CreateReviews, id=reviewId)

        try:
            likeReview = LikeReviews.objects.get(user__id=request.user.id, review__id=review.id)
        except LikeReviews.DoesNotExist:
            likeReview = None
        if (
            likeReview
        ):
            likeReview.delete()
        else:
            likeReview = LikeReviews.objects.create(review=review, user=request.user, like_unlike=True)
        return HttpResponseRedirect('/reviews')

