from django.urls import path
from wishlist import views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path("<int:id>", views.index, name="index"),
    path("delete/<int:id>", views.delete_wishlist, name="delete_wishlist"),
    path("remove/<int:id>", views.remove_book, name="remove_book"),
    path("transfer/<int:bookid>", views.move_book, name="move_book"),
    path("movetocart/<int:bookid>", views.move_to_cart, name="move_to_cart"),

]
