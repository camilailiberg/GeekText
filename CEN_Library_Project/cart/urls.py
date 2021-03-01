from django.urls import path
from cart import views

urlpatterns = [
    path("<int:cartitemid>", views.delete_cart_item, name="deletecartitem"),  # this connects to the
    # views in cart app
    path("sfl/<int:cartitemid>", views.save_for_later, name="saveforlater"),  # this connects to the
    # views in cart app
    path("mtc/<int:cartitemid>", views.move_to_cart, name="movetocart"),  # this connects to the
    # views in cart app
    # path("ShoppingCart/updateqnty/<int:cartitemid>", vcart.update_quantity, name="updateqty"),  # FIXME: Didn't work
    #  FIXME: CONTINUATION trying to update quantity
    # path('ShoppingCart/', CartView.as_view(), name='cart'),
    path('', views.shoppingcartview, name='cart'),  # this connects to the
    # views in cart app
]
