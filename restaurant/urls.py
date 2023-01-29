from . import views
from django.urls import path


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('menu', views.Menu.as_view(), name='menu'),
]
