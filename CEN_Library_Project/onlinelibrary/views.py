from django.shortcuts import render


# Create your views here.

def home(response):
    user = response.user
    return render(response, "onlinelibrary/home.html", {"user": user})

