from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import WishList
from bookdetails.models import Book


# Create your views here.

def index(response, id):
    ls = WishList.objects.get(id=id)
    bk = Book.objects.all()
    return render(response, "wishlist/list.html", {"bk": bk, "ls": ls})


def wishlist(response):
    userid = response.user.id
    wl = WishList.objects.all()

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("new"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                wl.create(name=txt, primary=False)
            else:
                print("invalid")

    return render(response, "wishlist/wishlisthome.html", {"wl": wl})


def delete_wishlist(response):
    userid = response.user.id
    wishlist = WishList.objects.all()
    wishlist.delete()

    wishlist.save()

    return redirect('/WishList/')


def delete_book(response, bookid):
    userid = response.user.id
    wishlist = WishList.objects.all()
    book = Book.objects.get(id=bookid)
    book.delete()

    wishlist.save()

    return redirect('/WishList/')


def move_book(response, bookid):
    userid = response.user.id
    wishlist = WishList.objects.get(id=userid)
    book = Book.objects.get(id=bookid)
    book.save()

    wishlist.save()

    return redirect('/wishlist/')
