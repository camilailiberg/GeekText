from django.urls import path
from . import views

from .views import CartView

urlpatterns = [
    path("", views.home, name="login"),
    path("ShoppingCart/<int:cartitemid>", views.delete_cart_item, name="deletecartitem"),
    path("ShoppingCart/sfl/<int:cartitemid>", views.save_for_later, name="saveforlater"),
    path("ShoppingCart/mtc/<int:cartitemid>", views.move_to_cart, name="movetocart"),
    # path('ShoppingCart/', CartView.as_view(), name='cart'),
    path('ShoppingCart/', views.shoppingcartview, name='cart'),
]
