from django.urls import path
from wishlist import views

urlpatterns = [
    path("<int:id>", views.index, name="index"),
    path("", views.wishlist, name="wishlist"),
]
