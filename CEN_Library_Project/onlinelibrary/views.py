from django.shortcuts import render


# Create your views here.
def login(response):
    return render(response, "onlinelibrary/home.html", {})


def shoppingcartview(response):
    return render(response, "onlinelibrary/shoppingcart.html", {})
