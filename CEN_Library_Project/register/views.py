from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import generic
from .models import Profile
from django.contrib.auth import login, authenticate
from django.contrib import messages


def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()

            return redirect("login")
    else:
        form = RegisterForm(response.POST)

    return render(response, "register/register.html", {"form": form})


def edit(response):
    userid = response.user.id
    profile = Profile.objects.get(id=userid)
    user = response.user
    return render(response, "registration/edit_profile.html", {"user": user, "profile": profile})


# here
def edit_username(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        user.username = request.POST['username']
        user.save()
    return redirect('/register/account')


def edit_email(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        user.email = request.POST['email']
        user.save()
    return redirect('/register/account')


def edit_first_name(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        user.first_name = request.POST['firstname']
        user.save()
    return redirect('/register/account')


def edit_last_name(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        user.last_name = request.POST['lastname']
        user.save()
    return redirect('/register/account')


def edit_home_address(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        profile.homeAddress = request.POST['homeaddress']
        profile.save()
    return redirect('/register/account')


def edit_address(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    if request.method == "POST":
        profile.address = request.POST['address']
        profile.save()
    return redirect('/register/account')


def account(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    return render(request, "registration/account_summary.html", {"user": user, "profile": profile})
