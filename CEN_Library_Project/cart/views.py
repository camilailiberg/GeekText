from django.shortcuts import render, redirect
from .models import ShoppingCart, ShoppingCartItem


# Create your views here.
def shoppingcartview(response):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    if cart == response.user.shoppingcart:
        total = cart.subtotal()

        return render(response, "cart/shoppingcart.html", {"cart": cart, "total": total})

    message = "You tried to access an unautharized shopping cart"
    return render(response, "onlinelibrary/home.html", {"message": message})


def delete_cart_item(request, cartitemid):
    userid = request.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    if request.method == "POST":
        cartitem.delete()
        cart.save()
        return redirect('/ShoppingCart/')

    return render(request, "cart/deletecartitem.html", {"cartitem":cartitem})


def save_for_later(response, cartitemid):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)
    cartitem.savedforlater = True
    cartitem.save()

    cart.save()

    return redirect('/ShoppingCart/')


def move_to_cart(response, cartitemid):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)

    cartitem.savedforlater = False
    cartitem.save()

    cart.save()

    return redirect('/ShoppingCart/')


# def update_quantity(response, cartitemid):
#     userid = response.user.id
#     cart = ShoppingCart.objects.get(id=userid)
#     cartitem = ShoppingCartItem.objects.get(id=cartitemid)
# #     form = response.form  # TODO: old
# #
#     if response.method == "POST":  # TODO: old
#         # cartitem.quantity += form.cleaned_data['quantity']  # TODO: old
#         if response.POST.get("quantity"):  # FIXME: trying and failed
#             newquantity = response.POST.get("quantity")  # FIXME: trying and failed
#             if newquantity > 0:  # FIXME: trying and failed
#                 cartitem.quantity = newquantity  # FIXME: trying and failed
#                 cartitem.save()  # TODO: old
#             else:  # FIXME: trying and failed
#                 print("invalid quantity")  # FIXME: trying and failed
#         # cartitem.save()  # TODO: old
#
#     cart.save()  # FIXME: trying and failed
#
#     return redirect('/ShoppingCart/')  # TODO: old


