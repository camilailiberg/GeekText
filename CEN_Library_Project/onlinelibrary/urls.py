from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="login"),
    path("ShoppingCart/", views.shoppingcartview, name="ShoppingCart"),
]
