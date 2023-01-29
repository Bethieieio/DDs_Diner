from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu', views.Menu.as_view(), name='menu'),
    path('reviews', views.Reviews.as_view(), name="reviews"),
    path('book_a_table', views.BookingCreation.as_view(), name="book_a_table"),
    path('your_bookings', views.ClientAdmin.as_view(), name="your_bookings"),
]
