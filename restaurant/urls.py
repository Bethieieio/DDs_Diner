from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('reviews', views.Reviews.as_view(), name='reviews'),
    path('book_a_table', views.BookingCreation.as_view(), name='book_a_table'),
    path('your_bookings', views.ClientAdmin.as_view(), name='your_bookings'),
    path(
        'your_bookings/<int:id>',
        views.BookingEdit.as_view(),
        name='edit_booking',
    ),
    path(
        'delete/<int:id>',
        views.BookingDelete.as_view(),
        name='delete_booking',
    ),
    path(
        'review_like/<int:reviewId>',
        views.LikeReview.as_view(),
        name='review_like',
    ),
]
