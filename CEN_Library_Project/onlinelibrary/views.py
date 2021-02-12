from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(response):
    return HttpResponse("<h1>Tech with Ernesto!!!!</h1>")

def wishlist(response):
    return HttpResponse("<h1>wishlist!!!!</h1>")
