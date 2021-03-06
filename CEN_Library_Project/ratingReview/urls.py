from django.shortcuts import render
from django.http import HttpResponse
from . import views
from django.urls import path

# Create your views here.

urlpatterns = [
    path("", views.rating_create_view),
]
