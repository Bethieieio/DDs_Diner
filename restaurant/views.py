from django.shortcuts import render
from django.views import generic, View

# Create your views here.


class Home(View):
    def get(self, request):
        
        return render(
            request,
            "index.html",
        )


class Menu(View):
    def get(self, request):

        return render(
            request,
            "menu.html",
        )