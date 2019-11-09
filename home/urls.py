#from django.urls import path, re_path
from django.conf.urls import url, include

from views import *

urlpatterns = [
    url(r'^$', indexView, name="indexView"),
    url(r'^login$', loginView, name="loginView"),
    url(r'^logout$', logout, name="logout"),
    url(r'^check_account$', checkAccount, name='checkAccount')
]
