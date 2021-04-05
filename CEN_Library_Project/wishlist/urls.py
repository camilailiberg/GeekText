from django.urls import path
from wishlist import views

urlpatterns = [
    path("", views.wishlist, name="wishlist"),
    path("<int:id>", views.index, name="indexwl"),
    path("delete/<int:id>", views.delete_wishlist, name="delete_wishlist"),
    path("remove/<int:id>", views.remove_book, name="remove_book"),
    path("transfer/<int:bookid>", views.move_book, name="move_book"),
    path("movetocart/<int:bookid>", views.move_to_cart, name="move_to_cart"),
    path("transferbook/<int:fromwishlistid>/<int:towishlistid>/<int:bookid>", views.transfer_book, name="transfer_book"),
    path("addbooktowishlist/<int:towishlistid>/<int:bookid>", views.add_book_to_wishlist, name="add_book_to_wishlist"),
    path("setprimary/<int:wishlistid>", views.set_primary, name="set_primary"),
    path("removeprimary/", views.remove_primary, name="remove_primary"),
]
