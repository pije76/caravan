from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.indexView, name="indexView"),
    path("login", views.loginView, name="loginView"),
    path("logout", views.logout, name="logout"),
    path("check_account", views.checkAccount, name="checkAccount"),
]