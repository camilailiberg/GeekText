from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from . import views
from django.urls import path

# Create your views here.

urlpatterns = [
    path('<int:book_id>/', views.index, name='index'),
    path('<str:author>/', views.similar, name='similar'),
    path("movebooktocart/<int:bookid>", views.move_book_to_cart, name="move_book_to_cart"),
]
