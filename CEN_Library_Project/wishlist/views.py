from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from .models import WishList
from register.models import Profile
from bookdetails.models import Book
from cart.models import ShoppingCart
from cart.models import ShoppingCartItem

# Create your views here.


def index(response, id):  # good to go
    wl = WishList.objects.get(id=id)
    global wishlist_id
    wishlist_id = id
    bk = wl.book.all()
    return render(response, "wishlist/list.html", {"wl":wl, "bk": bk})


def wishlist(response):  # good to go
    wl = WishList.objects.filter(user=response.user)
    counter = 0
    counter2 = 0

    if response.method == "POST":
        print(response.POST)
        if response.POST.get("new"):
            txt = response.POST.get("new")
            if len(txt) > 2:
                if response.user.profile.wishlistCounter < 3:
                    response.user.profile.addWishlist()
                    response.user.profile.save()
                    wl.create(name=txt, primary=False, user=response.user)
                    return redirect('/wishlist/')
                else:
                    message = "Oops! You cannot have more than 3 wish lists."
                    for i in message:
                        counter += 1
                    return render(response, "wishlist/wishlisthome.html", {"wl": wl, "counter": counter, "message": message})
                    raise Exception("Maximum number of List")
            else:
                message2 = "Oops! The name for your list is too short, it must contain at least 3 letters."
                for i in message2:
                    counter2 += 1
                return render(response, "wishlist/wishlisthome.html",
                              {"wl": wl, "counter2": counter2, "message2": message2})
                raise Exception("Invalid Name")

    return render(response, "wishlist/wishlisthome.html", {"wl": wl})


def set_primary(request, wishlistid):
    wl = WishList.objects.filter(user=request.user)

    if request.method == 'POST':
        userlists = WishList.objects.all()
        for l in userlists:
            if l.user == request.user and l.primary:
                l.primary = False
                l.save()
        setprimarywishlist = WishList.objects.get(id=wishlistid)
        setprimarywishlist.primary = True
        setprimarywishlist.save()
        wl = WishList.objects.filter(user=request.user)
        return render(request, "wishlist/wishlisthome.html", {"wl": wl})

    else:
        return render(request, "wishlist/wishlisthome.html", {"wl": wl})


def remove_primary(request):
    wl = WishList.objects.filter(user=request.user)

    if request.method == 'POST':
        userlists = WishList.objects.all()
        for l in userlists:
            if l.user == request.user and l.primary:
                l.primary = False
                l.save()
        wl = WishList.objects.filter(user=request.user)
        return render(request, "wishlist/wishlisthome.html", {"wl": wl})

    else:
        return render(request, "wishlist/wishlisthome.html", {"wl": wl})


def delete_wishlist(request, id):  # good to go
    wl = WishList.objects.get(id=id)
    if request.method == "POST":
        wl.delete()
        request.user.profile.wishlistCounter = request.user.profile.wishlistCounter - 1
        request.user.profile.save()
        return redirect('/wishlist/')

    return render(request, "wishlist/delete.html", {'wl': wl})


def remove_book(request, id):  # good to go
    wl = WishList.objects.get(id=wishlist_id)
    bk = wl.book.get(id=id)
    if request.method == "POST":
        wl.book.remove(bk)
        return redirect('indexwl', wl.id)

    return render(request, 'wishlist/remove.html', {"bk": bk, "wl": wl})


def move_book(request, id):
    wl = WishList.objects.get(id=wishlist_id)
    bk = wl.book.get(id=id)
    if request.method == "POST":
        wl.book.id = wishlist_id
        return redirect('/wishlist/')

    return render(request, 'wishlist/transfer.html', {"bk": bk})


def move_to_cart(response, bookid):
    userid = response.user.id
    wl = WishList.objects.get(id=wishlist_id)
    bk = Book.objects.get(id=bookid)
    cart = ShoppingCart.objects.get(id=userid)

    # for every shoppingcartitem in the cart object of the user
    for item in cart.shoppingcartitem_set.all():
        #  if the item is not marked as ordered and the book saved in the shoppingcartitem object
        # is the same book that we are moving from wishlist
        if item.ordered == False and item.book == bk:
            item.quantity = item.quantity + 1  # Update the quantity of that shippingcartitem
            if item.savedforlater: #  if the shoppingcartitem object that holds the book being moved is in the
                # saved for later section of the shopping cart
                item.savedforlater = False #  take it out of the saved for later section and move it to the main
                # section of the shopping cart
            item.save()
            cart.save()
            wl.book.remove(bk)
            return redirect('indexwl', wl.id)
    cartitem = ShoppingCartItem.objects.all()
    cartitem.create(shoppingcart=cart, book=bk, quantity=1, ordered=False, savedforlater=False)
    wl.book.remove(bk)
    return redirect('indexwl', wl.id)


def transfer_book(request, fromwishlistid, towishlistid, bookid):
    userid = request.user.id
    allWishLists = WishList.objects.all()
    wl = WishList.objects.get(id=fromwishlistid)
    tolist = WishList.objects.get(id=towishlistid)
    bk = Book.objects.get(id=bookid)

    if request.method == 'POST':
        wl.book.remove(bk)
        tolist.book.add(bk)
        wl.save()
        tolist.save()
        return redirect('indexwl', tolist.id)

    return render(request, 'wishlist/transfer_book.html', {"allWishLists": allWishLists, "wl": wl, "bk": bk})


def add_book_to_wishlist(request, towishlistid, bookid):
    userid = request.user.id
    allWishLists = WishList.objects.all()
    bk = Book.objects.get(id=bookid)

    if request.method == 'POST':
        tolist = WishList.objects.get(id=towishlistid)
        tolist.book.add(bk)
        tolist.save()
        return redirect('indexwl', tolist.id)

    return render(request, 'wishlist/add_book_to_wishlist.html', {"allWishLists": allWishLists, "bk": bk})
