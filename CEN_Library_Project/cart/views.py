from django.shortcuts import render, redirect
from .models import ShoppingCart, ShoppingCartItem

from django.views.generic import TemplateView, DeleteView
from .forms import CartForm


# Create your views here.
def shoppingcartview(response):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    # form = CartForm()

    if cart == response.user.shoppingcart:
        total = cart.subtotal()

        # return render(response, "onlinelibrary/shoppingcart.html", {"cart": cart, "total": total, "form": form})
        return render(response, "cart/shoppingcart.html", {"cart": cart, "total": total})

    message = "You tried to access an unautharized shopping cart"
    return render(response, "onlinelibrary/home.html", {"message": message})


def delete_cart_item(response, cartitemid):
    userid = response.user.id
    cart = ShoppingCart.objects.get(id=userid)
    cartitem = ShoppingCartItem.objects.get(id=cartitemid)
    cartitem.delete()

    cart.save()

    return redirect('/ShoppingCart/')


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
#     form = response.form
#
#     if response.method == "POST":
#         cartitem.quantity += form.cleaned_data['quantity']
#         cartitem.save()
#
#     cart.save()
#
#     return redirect('/ShoppingCart/')


class CartView(TemplateView):
    template_name = 'cart/shoppingcart.html'

    def get(self, response):
        form = CartForm()

        userid = response.user.id
        cart = ShoppingCart.objects.get(id=userid)

        if cart == response.user.shoppingcart:
            total = cart.subtotal()

        args = {'form': form, 'total': total, 'cart': cart}
        return render(response, self.template_name, args)

    def post(self, response):
        form = CartForm(response.POST)

        userid = response.user.id
        cart = ShoppingCart.objects.get(id=userid)

        if cart == response.user.shoppingcart:
            total = cart.subtotal()

            if form.is_valid():
                shoppingcartitem = form.save(commit=False)
                shoppingcartitem.user = response.user
                shoppingcartitem.save()
                quantity = form.cleaned_data['quantity']
                savedforlater = form.cleaned_data['savedforlater']

        args = {'form': form, 'quantity': quantity, 'savedforlater': savedforlater, 'total': total, 'cart': cart}
        return render(response, self.template_name, args)
