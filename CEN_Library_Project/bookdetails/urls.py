from django.shortcuts import render
from .models import Book
from django.http import HttpResponse
from . import views
from django.urls import path

# Create your views here.

urlpatterns = [
    path('', views.index, name='bookdetails'),
]
