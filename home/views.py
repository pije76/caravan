from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as django_login
from django.contrib.auth import logout as django_logout
from django.http import HttpResponse

from database.models import TblUser


# ***********************************************************************************
# @function: Index View
# -----------------------------------------------------------------------------------
@login_required
def indexView(request):
    email = request.session.get("email")
    user_obj = TblUser.objects.get(username=email)
    if user_obj.is_superuser == 1:
        return redirect("/admin")
    else:
        return redirect("/user")


# ***********************************************************************************
# @function: Login View
# -----------------------------------------------------------------------------------
def loginView(request, template_name="home/login.html"):
    try:
        return render(request, template_name)
    except Exception as e:
        return redirect("/")


# ***********************************************************************************
# @function: Log Out
# -----------------------------------------------------------------------------------
@login_required
def logout(request):
    request.session.clear()
    django_logout(request)
    return redirect("/")


# ***********************************************************************************
# @function: Check Account
# -----------------------------------------------------------------------------------
def checkAccount(request):
    try:
        email = request.POST["email"]
        password = request.POST["password"]
        user = authenticate(request, username=email, password=password)
        if user == None:
            return redirect("/login")
        django_login(request, user)
        request.session["email"] = email
        return redirect("/")
    except Exception as e:
        return redirect("/login")
