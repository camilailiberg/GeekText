from django.urls import path
from . import views

urlpatterns = [
    path("wishlist/<int:id>", views.index, name="index"),
    path("wishlist", views.wishlist, name="wishlist"),
]
