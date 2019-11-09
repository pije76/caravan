from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.indexView, name="indexView"),
    path("register_user", views.registerUser, name="registerUser"),
    path("update_user", views.updateUser, name="updateUser"),
    path("delete_user", views.deleteUser, name="deleteUser"),
    path("get_page_content", views.getPageUsers, name="getPageUsers")
]