#from django.urls import path, re_path
from django.conf.urls import url, include

from . import views

urlpatterns = [
#    url("", views.indexView, name="indexView"),
    url("register_user", views.registerUser, name="registerUser"),
    url("update_user", views.updateUser, name="updateUser"),
    url("delete_user", views.deleteUser, name="deleteUser"),
    url("get_page_content", views.getPageUsers, name="getPageUsers")
]
