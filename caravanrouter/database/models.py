from django.db import models
from django.contrib.auth.models import AbstractUser

class TblUser(AbstractUser):
    uid = models.BigIntegerField(null=False)
    type = models.IntegerField()
    s_password = models.CharField(max_length=255, default="password")
    phone = models.CharField(max_length=100, default="")
    mobile = models.CharField(max_length=100, default="")
    billing_address = models.CharField(max_length=255, default="{}")
    shipping_address = models.CharField(max_length=255, default="{}")
    iccid = models.CharField(max_length=100, default="")
    consumer_id = models.CharField(max_length=100, default="")
    language = models.IntegerField(default=1)
    invoice_nr = models.CharField(max_length=100, default="")
    order_nr = models.CharField(max_length=100, default="")
    subscr_month = models.IntegerField(default=6)
    subscr_data = models.IntegerField(default=5)
    subscr_type = models.IntegerField(default=1)
    note = models.TextField(max_length=1024, default="")



class TblMenu(models.Model):
    name = models.CharField(max_length=100, default="")
    parent_id = models.IntegerField()
    has_child = models.IntegerField()
    icon = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    privilege = models.IntegerField()



class TblTrafficData(models.Model):
    iccid = models.CharField(max_length=100, default="")
    date = models.DateField()
    traffic = models.FloatField()



class TblIccidList(models.Model):
    iccid = models.CharField(max_length=100, default="")
    status = models.IntegerField(default=1)
