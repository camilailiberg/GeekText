from django.shortcuts import render
from django.http import HttpResponse
from .models import WishList, Book


# Create your views here.

def index(response, id):
    ls = WishList.objects.get(id=id)
    return render(response, "onlinelibrary/List.html", {"ls": ls})

def wishlist(response):
    wl = WishList.objects.all()

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("new"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                wl.create(name=txt, primary=False)
            else:
                print("invalid")

    return render(response, "onlinelibrary/WishListHome.html", {"wl": wl})

