from django.shortcuts import render


# Create your views here.
<<<<<<< HEAD
def home(response):
    user = response.user
    return render(response, "onlinelibrary/home.html", {"user": user})
=======
def index(request):
    return render(request, 'onlinelibrary/index.html', {})
>>>>>>> origin/Browse_Sort
