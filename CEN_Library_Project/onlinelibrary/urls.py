from django.urls import path
# from . import views
from browse import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
]
