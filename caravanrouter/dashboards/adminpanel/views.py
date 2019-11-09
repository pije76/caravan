import json
import math

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from caravanrouter.database.models import *

# ***********************************************************************************
# @function: Get Language String From Its Id
# -----------------------------------------------------------------------------------
def getLanguageStr(language_id):
    if language_id == 1:
        return "English"
    elif language_id == 2:
        return "Spanish"
    elif language_id == 3:
        return "Swedish"


# ***********************************************************************************
# @function: Get total users
# -----------------------------------------------------------------------------------
def getTotalUsers(except_email, filter_str):
    user_list = list(TblUser.objects.filter().exclude(username=except_email))
    res = []
    for user in user_list:
        flg = False
        if user.first_name.find(filter_str) != -1:
            flg = True
        if user.last_name.find(filter_str) != -1:
            flg = True
        if user.phone.find(filter_str) != -1:
            flg = True
        if user.mobile.find(filter_str) != -1:
            flg = True
        if user.iccid.find(filter_str) != -1:
            flg = True
        if user.consumer_id.find(filter_str) != -1:
            flg = True

        if flg == False:
            continue

        bill_address = json.loads(user.billing_address)
        shipping_address = json.loads(user.shipping_address)
        reg_date = str(user.date_joined.year) + "/" + str(user.date_joined.month) + "/" + str(user.date_joined.day)
        res.append({
            "id": user.id,
            "name": user.first_name,
            "surname": user.last_name,
            "type": user.type,
            "language": user.language,
            "invoice_nr": user.invoice_nr,
            "order_nr": user.order_nr,
            "phone": user.phone,
            "mobile": user.mobile,
            "email": user.username,
            "password": user.s_password,
            "bill_address1": bill_address["address1"],
            "bill_address2": bill_address["address2"],
            "bill_country": bill_address["country"],
            "bill_city": bill_address["city"],
            "bill_state": bill_address["state"],
            "bill_postalcode": bill_address["postalcode"],
            "shipping_address1": shipping_address["address1"],
            "shipping_address2": shipping_address["address2"],
            "shipping_country": shipping_address["country"],
            "shipping_city": shipping_address["city"],
            "shipping_state": shipping_address["state"],
            "shipping_postalcode": shipping_address["postalcode"],
            "iccid": user.iccid,
            "consumer_id": user.consumer_id,
            "subscr_month": user.subscr_month,
            "subscr_data": user.subscr_data,
            "subscr_type": user.subscr_type,
            "note": user.note.replace("\n", "slashn").replace("\\", "slashopposite"),
            "reg_date": reg_date,
        })
    return res


# ***********************************************************************************
# @function: Index view
# -----------------------------------------------------------------------------------
@login_required
def indexView(request):
    email = request.session.get("email")
    user_obj = TblUser.objects.get(username=email)
    user_list = getTotalUsers(email, "")
    total_user = len(user_list)
    user_list = user_list[0:15]

    page_text = {
        "contact": "Contact",
        "shop": "Shop",
        "profile": "Profile",
        "close": "Close",
        "logout": "Logout",
        "email": "Email",
        "password": "Password",
    }
    return render(request, "adminpanel/dashboard.html", {
                            "email": email,
                            "password": user_obj.s_password,
                            "user_list": user_list,
                            "total_user": total_user,
                            "total_page": math.ceil(total_user / 15),
                            "page_text": page_text,
                        })


# ***********************************************************************************
# @function: Get page users
# -----------------------------------------------------------------------------------
@login_required
def getPageUsers(request):
    try:
        cur_page = int(request.POST["cur_page"])
        filter_name = request.POST["filter_name"]
        email = request.session.get("email")
        user_list = getTotalUsers(email, filter_name)
        total_user = len(user_list)
        user_list = user_list[15*(cur_page - 1):15*cur_page]
        return HttpResponse(json.dumps({
            "user_list": user_list,
            "total_page": math.ceil(total_user/15)
        }))

    except Exception as e:
        return HttpResponse("error", status=500)


# ***********************************************************************************
# @function: Register user
# -----------------------------------------------------------------------------------
@login_required
def registerUser(request):
    try:
        data = json.loads(request.POST["param"])

        # ---------- duplication check ---------- #
        user_obj = list(TblUser.objects.filter(email=data["email"]))
        if len(user_obj) > 0:
            return HttpResponse("existing_email", stauts=500)
        user_obj = list(TblUser.objects.filter(consumer_id=data["consumer_id"]))
        if len(user_obj) > 0:
            return HttpResponse("existing_consumer_id", status=500)

        user_obj = TblUser()
        user_obj.username = data["email"]
        user_obj.email = data["email"]
        user_obj.s_password = data["password"]
        user_obj.first_name = data["name"]
        user_obj.last_name = data["surname"]
        user_obj.type = int(data["type"])
        user_obj.language = int(data["language"])
        user_obj.invoice_nr = data["invoice_nr"]
        user_obj.order_nr = data["order_nr"]
        user_obj.phone = data["phone"]
        user_obj.mobile = data["mobile"]
        user_obj.billing_address = data["billing_address"]
        user_obj.shipping_address = data["shipping_address"]
        user_obj.iccid = data["iccid"]
        user_obj.consumer_id = data["consumer_id"]
        user_obj.subscr_month = data["subscr_month"]
        user_obj.subscr_data = data["subscr_data"]
        user_obj.subscr_type = data["subscr_type"]
        user_obj.note = data["note"]
        user_obj.is_superuser = 0
        user_obj.is_active = 1
        user_obj.uid = 0
        user_obj.set_password(data["password"])
        user_obj.save()

        # ---------- get iccid list and store ---------- #
        try:
            iccid_list = data["iccid"].split(",")
            for iccid in iccid_list:
                iccid_obj = list(TblIccidList.objects.filter(iccid=iccid))
                if len(iccid_obj) != 0:
                    continue
                iccid_obj = TblIccidList()
                iccid_obj.iccid = iccid
                iccid_obj.status = 1
                iccid_obj.save()

        except Exception as e1:
            user_obj = TblUser.objects.get(email=data["email"])
            user_obj.delete()
            user_obj.save()
            return HttpResponse("unknown_error", status=500)

        reg_date = str(user_obj.date_joined.year) + "/" + str(user_obj.date_joined.month) + "/" + str(user_obj.date_joined.day)
        return HttpResponse(json.dumps({
            "id": user_obj.id,
            "reg_date": reg_date,
        }), status=200)

    except Exception as e:
        return HttpResponse("unknown_error", status=500)


# ***********************************************************************************
# @function: Register user
# -----------------------------------------------------------------------------------
def updateUser(request):
    try:
        data = json.loads(request.POST["param"])

        # ---------- duplication check ---------- #
        user_obj = list(TblUser.objects.filter(consumer_id=data["consumer_id"]).exclude(email=data["email"]))
        if len(user_obj) > 0:
            return HttpResponse("existing_consumer_id", status=500)


        user_obj = TblUser.objects.get(email=data["email"])
        user_obj.s_password = data["password"]
        user_obj.first_name = data["name"]
        user_obj.last_name = data["surname"]
        user_obj.type = int(data["type"])
        user_obj.language = int(data["language"])
        user_obj.invoice_nr = data["invoice_nr"]
        user_obj.order_nr = data["order_nr"]
        user_obj.phone = data["phone"]
        user_obj.mobile = data["mobile"]
        user_obj.billing_address = data["billing_address"]
        user_obj.shipping_address = data["shipping_address"]
        user_obj.iccid = data["iccid"]
        user_obj.consumer_id = data["consumer_id"]
        user_obj.subscr_month = data["subscr_month"]
        user_obj.subscr_data = data["subscr_data"]
        user_obj.subscr_type = data["subscr_type"]
        user_obj.note = data["note"]
        user_obj.set_password(data["password"])
        user_obj.save()

        # ---------- get iccid list and store ---------- #
        try:
            iccid_list = data["iccid"].split(",")
            for iccid in iccid_list:
                iccid_obj = list(TblIccidList.objects.filter(iccid=iccid))
                if len(iccid_obj) != 0:
                    continue
                iccid_obj = TblIccidList()
                iccid_obj.iccid = iccid
                iccid_obj.status = 1
                iccid_obj.save()

        except Exception as e1:
            return HttpResponse("unknown_error", status=500)

        return HttpResponse("success")
    except Exception as e:
        return HttpResponse("unknown_error", status=500)


# ***********************************************************************************
# @function: Delete User
# -----------------------------------------------------------------------------------
def deleteUser(request):
    try:
        user_id = request.POST["id"]
        user_obj = TblUser.objects.get(id=user_id)
        user_obj.delete()
        return HttpResponse("success")
    except Exception as e:
        return HttpResponse("error", status=500)
