from django.urls import path
from . import views

<<<<<<< HEAD

urlpatterns = [
    path("", views.home, name="home"),
]
=======
urlpatterns = [
    path('', views.index, name='index'),
]
>>>>>>> origin/Browse_Sort
