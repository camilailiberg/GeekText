"""CEN_Library_Project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin

from django.urls import path, include  # , re_path  # re_path ADDED FOR ANGULAR
from register import views as v
from django.conf import settings

from django.conf.urls.static import static, serve  # serve added FOR ANGULAR
from rest_framework.routers import DefaultRouter

import onlinelibrary.api_views

urlpatterns = [
    path('', include('onlinelibrary.urls')),
    path('admin/', admin.site.urls),

    #  REGISTER APP VIEWS:
    path("register/", v.register, name="register"),  # this connects to the views inside register app
    path('', include("django.contrib.auth.urls")),  # this goes to django.contrib.auth.urls application, it will look
    # in the url file there and will see if we have a valid url, so it will se if we have something like "login"
    # "logout "change-password" "create-password" etc. So what we need to do is create a registration folder called
    # registration and put login.html in there because that is where django is going to look and what template we will
    # use to render our login form.

    #  CART APP URLS:
    path('ShoppingCart/', include("cart.urls")),  # this connects to the urls.py inside the app cart

    #  WISHLIST APP URLS:
    path('wishlist/', include("wishlist.urls")),  # this connects to the urls.py inside the app wishlist

    # ONLINELIBRARY APP URLS
    path('', include("onlinelibrary.urls")),  # this connects to the urls.py inside the app onlinelibrary


    #  RESTful API VIEWS FOR SHOPPINGCARTITEMS
    path('api/v1/shoppingcartitems/', onlinelibrary.api_views.ShoppingCartItemList.as_view()),  # This is for the
    # RESTful api views for the shoppingcartapi
    path('api/v1/shoppingcartitems/new', onlinelibrary.api_views.ShoppingCartItemCreate.as_view()),  # This is for the
    # RESTful api views for the shoppingcartapi
    path('api/v1/shoppingcartitems/<int:id>/',  # This is for the  RESTful api views for the shoppingcartapi
         onlinelibrary.api_views.ShoppingCartItemRetriveUpdateDestroy.as_view()),  # This is for the  RESTful api views
    # for the shoppingcartapi


    path('bookdetails/', include('bookdetails.urls')),

    path('browse/', include('browse.urls')),
]
