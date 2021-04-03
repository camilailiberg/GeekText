from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from . import views
from django.urls import path

# Create your views here.
app_name = 'bookdetails'
urlpatterns = [
    path('<int:book_id>', views.index, name='index'),
    path('', views.home, name='home'),
]
