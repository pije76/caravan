#from django.urls import path, re_path
from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'', views.indexView, name="indexView"),
    url("login", views.loginView, name="loginView"),
#    url("logout", views.logout, name="logout"),
#    url("check_account", views.checkAccount, name="checkAccount"),
]
