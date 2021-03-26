from django.utils.timezone import get_current_timezone
from datetime import datetime
from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.views import generic
from .models import Profile, CreditCard
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.utils.dateparse import parse_datetime

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


def add_credit_card_info(request):
    userid = request.user.id
    profile = Profile.objects.get(id=userid)
    user = request.user
    wrongformat = False
    message = False
    invalidcardnumber = False
    invalidsecuritynumber = False

    if request.method == "POST":
        cardnumber = request.POST['cardnumber']
        if int(cardnumber) < 1000000000000:
            invalidcardnumber = True
            return render(request, "registration/add_credit_card.html",
                          {"user": user, "profile": profile, "invalidcardnumber": invalidcardnumber})
        expiration = request.POST['expirationdate']
        try:
            datetime_object = datetime.strptime(expiration, "%Y-%m-%d")
        except ValueError:
            wrongformat = True
            return render(request, "registration/add_credit_card.html",
                          {"user": user, "profile": profile, "wrongformat": wrongformat})
        # datetime_object = datetime.strptime(expiration, "%Y-%m-%d")
        securitynumber = request.POST['securitynumber']
        if int(securitynumber) < 100:
            invalidsecuritynumber = True
            return render(request, "registration/add_credit_card.html",
                          {"user": user, "profile": profile, "invalidsecuritynumber": invalidsecuritynumber})
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        if datetime_object < datetime.today():
            message = True
            return render(request, "registration/add_credit_card.html", {"user": user, "profile": profile, "message":message})
            raise Exception("Ups! Your credit card number either is expired or expires today.")
        CreditCard.objects.create(profile=profile, cardnumber=cardnumber, expiration=expiration,
                                  security=securitynumber, firstname=firstname, lastname=lastname)
        return redirect('/register/payment_information')

    return render(request, "registration/add_credit_card.html", {"user": user, "profile": profile})


def payment_info(response):
    userid = response.user.id
    profile = Profile.objects.get(id=userid)
    user = response.user
    return render(response, "registration/payment_information.html", {"user": user, "profile": profile})
