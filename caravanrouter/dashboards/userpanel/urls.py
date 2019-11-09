from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path("", views.indexView, name="indexView"),
    path("update_iccid", views.updateIccid, name="updateIccid"),
]