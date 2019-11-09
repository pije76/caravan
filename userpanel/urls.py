from django.conf.urls import url
#from django.urls import path

from . import views

urlpatterns = [
#    url("", views.indexView, name="indexView"),
    url("update_iccid", views.updateIccid, name="updateIccid"),
]
