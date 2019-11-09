import datetime
from dateutil.relativedelta import *

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

from calendar import monthrange

from caravanrouter.database.models import *
from caravanrouter.module.orangem2m import *

# ***********************************************************************************
# @function: Get Subscription Type String
# -----------------------------------------------------------------------------------
def getSubscrTypeString(subscr_type):
    if subscr_type == 1:
        return "National"
    elif subscr_type == 2:
        return "Roaming"


# ***********************************************************************************
# @function: Get Current Subscription Month Period
# -----------------------------------------------------------------------------------
def getCurSubscrMonthPeriod(subscr_start_date):
    today = datetime.datetime.today()

    # ---------- calculate current subscription month period ---------- #
    if today.day < subscr_start_date.day:
        cur_subscr_start_date = datetime.datetime(today.year, today.month, subscr_start_date.day)
        cur_subscr_start_date = cur_subscr_start_date + relativedelta(months=-1)
        cur_subscr_end_date = cur_subscr_start_date + relativedelta(months=1) + relativedelta(days=-1)
    else:
        cur_subscr_start_date = datetime.datetime(today.year, today.month, subscr_start_date.day)
        cur_subscr_end_date = cur_subscr_start_date + relativedelta(months=1) + relativedelta(days=-1)

    return cur_subscr_start_date, cur_subscr_end_date


# ***********************************************************************************
# @function: Index View
# -----------------------------------------------------------------------------------
@login_required
def indexView(request):
    try:
        email = request.session.get("email")
        user_obj = tbl_user.objects.get(username=email)
        iccid_list = user_obj.iccid.split(",")
        type = user_obj.type
        subscr_start_date = user_obj.date_joined
        subscr_end_date = user_obj.date_joined + relativedelta(months=user_obj.subscr_month) + relativedelta(days=-1)
        subscr_start_date = str(subscr_start_date.year) + "/" + str(subscr_start_date.month) + "/" + str(subscr_start_date.day)
        subscr_end_date = str(subscr_end_date.year) + "/" + str(subscr_end_date.month) + "/" + str(subscr_end_date.day)
        subscr_period = subscr_start_date + " - " + subscr_end_date

        today = datetime.datetime.today()

        # ---------- calculate current subscription month period ---------- #
        cur_subscr_start_date, cur_subscr_end_date = getCurSubscrMonthPeriod(user_obj.date_joined)
        left_days = (cur_subscr_end_date - datetime.datetime(today.year, today.month, today.day)).days

        page_text = {}

        if user_obj.language == 1:      ### English
            page_text = {
                "welcome": "Welcome to your Caravan Sim-Card overview page",
                "subscription": "Your subscription: " + str(user_obj.subscr_data) + "GB / " + str(user_obj.subscr_month) + " Month with " + getSubscrTypeString(user_obj.subscr_type),
                "subscr_period": subscr_period,
                "left_days": str(left_days) + " days until next period",
                "iccid_list": "ICCID List",
                "update": "Update",
                "update_iccid": "Update ICCID",
                "status": "Status",
                "activate": "Activate",
                "activated": "Activated",
                "block": "Block",
                "blocked": "Blocked",
                "suspend": "Suspend",
                "suspended": "Suspended",
                "confirm": "Confirm",
                "close": "Close",
                "total_left_month": "Total Data left to use this month",
                "total_used_month": "Total usage this month",
                "unit": "Unit",
                "traffic": "Traffic",
                "contact": "Contact",
                "shop": "Shop",
                "profile": "Profile",
                "logout": "Logout",
                "email": "Email",
                "password": "Password",

                "months": [
                    "January",
                    "Feburary",
                    "March",
                    "April",
                    "May",
                    "June",
                    "July",
                    "August",
                    "September",
                    "October",
                    "November",
                    "December"
                ]
            }
        elif user_obj.language == 2:           ### Swedish
            page_text = {
                "welcome": "Välkommen till Mina Sidor för Caravan Router",
                "subscription": "Ditt abonnemang: " + str(user_obj.subscr_data) + "GB / " + str(
                    user_obj.subscr_month) + " Månader förbrukning " + getSubscrTypeString(user_obj.subscr_type),
                "subscr_period": subscr_period,
                "left_days": str(left_days) + " days until next period",
                "iccid_list": "ICCID Lista",
                "update": "Uppdatera",
                "update_iccid": "Uppdatera ICCID",
                "status": "Status",
                "activate": "Aktiverad",
                "activated": "Aktiverad",
                "block": "Blocka",
                "blocked": "Blockerad",
                "suspend": "Suspendera",
                "suspended": "Suspenderad",
                "confirm": "Bekräfta",
                "close": "Stäng",
                "total_left_month": "Total data kvar att använda denna månaden",
                "total_used_month": "Total användning den här månaden",
                "unit": "Enhet",
                "traffic": "Traffik",
                "contact": "Kontakt",
                "shop": "Butik",
                "profile": "Profil",
                "logout": "Logga ut",
                "email": "E-post",
                "password": "Lösenord",

                "months": [
                    "Januari",
                    "Februari",
                    "Mars",
                    "April",
                    "Maj",
                    "Juni",
                    "Juli",
                    "Augusti",
                    "September",
                    "Oktober",
                    "November",
                    "December"
                ]
            }

        elif user_obj.language == 3:   ### Spanish
            page_text = {
                "welcome": "Bienvenido a tu Área Personal de Caravan Router ",
                "subscription": "Tu Suscripción: " + str(user_obj.subscr_data) + "GB / " + str(
                    user_obj.subscr_month) + " meses " + getSubscrTypeString(user_obj.subscr_type),
                "subscr_period": subscr_period,
                "left_days": str(left_days) + " days until next period",
                "iccid_list": "Lista de ICCID",
                "update": "Actualizar",
                "update_iccid": "Actualizar ICCID",
                "status": "Estado",
                "activate": "Activada",
                "activated": "Activada",
                "block": "Bloquear",
                "blocked": "Bloqueada",
                "suspend": "Suspender",
                "suspended": "Suspendida",
                "confirm": "Confirmar",
                "close": "Cerrar",
                "total_left_month": "Total de datos restantes para usar este mes",
                "total_used_month": "Uso total este mes",
                "unit": "Unidad",
                "traffic": "Tráfico",
                "contact": "Contacto",
                "shop": "Tienda",
                "profile": "Perfil",
                "logout": "Cerrar sesión",
                "email": "Email",
                "password": "Contraseña",

                "months": [
                    "Enero",
                    "Febrero",
                    "Marzo",
                    "Abril",
                    "Mayo",
                    "Junio",
                    "Julio",
                    "Agosto",
                    "Septiembre",
                    "Octubre",
                    "Noviembre",
                    "Diciembre"
                ]
            }

        # ---------- get usage data of this iccid ---------- #
        simcard_data = {}

        for iccid in iccid_list:
            simcard_data[iccid] = {
                "monthly_usage": {},
                "daily_usage": {},
                "total_traffic": 0,
                "status": "UNKNOWN",
            }

            # ---------- get current year's traffic by monthly ---------- #
            for month in range(1, 13):
                start_date = datetime.date(today.year, month, 1)
                end_date = datetime.date(today.year, month, monthrange(today.year, month)[1])
                tf_data = list(tbl_traffic_data.objects.filter(iccid=iccid, date__gte=start_date, date__lte=end_date))
                simcard_data[iccid]["monthly_usage"][str(month)] = 0
                for traffic in tf_data:
                    simcard_data[iccid]["monthly_usage"][str(month)] += traffic.traffic
                simcard_data[iccid]["monthly_usage"][str(month)] = simcard_data[iccid]["monthly_usage"][str(month)] / 1024 / 1024

            # ---------- get current month's traffic by daily ---------- #
            for day in range(1, monthrange(today.year, today.month)[1] + 1):
                start_date = datetime.date(today.year, today.month, day)
                tf_data = list(tbl_traffic_data.objects.filter(iccid=iccid, date=start_date))
                if len(tf_data) == 0:
                    simcard_data[iccid]["daily_usage"][str(day)] = 0
                else:
                    simcard_data[iccid]["daily_usage"][str(day)] = tf_data[0].traffic

            # ---------- get current subscription month's total traffic ---------- #
            start_date = cur_subscr_start_date
            end_date = cur_subscr_end_date
            tf_data = list(tbl_traffic_data.objects.filter(iccid=iccid, date__gte=start_date, date__lte=end_date))
            for traffic in tf_data:
                simcard_data[iccid]["total_traffic"] += traffic.traffic
            simcard_data[iccid]["total_traffic"] = format(round((simcard_data[iccid]["total_traffic"] / 1024 / 1024), 2), ",")

            simcard_data[iccid]["subscr_traffic"] = user_obj.subscr_data

        # ---------- get status of sim ---------- #
        sim_status = getSimStatus(iccid_list)
        for iccid in iccid_list:
            if str(iccid) in sim_status:
                simcard_data[iccid]["status"] = sim_status[str(iccid)]

        daily_chart_title = str(today.year) + "/" + str(today.month) + "/1 - " + str(today.year) + "/" + str(today.month) + "/" + str(monthrange(today.year, today.month)[1])
        monthly_chart_title = str(today.year) + "/1 ~ " + str(today.year) + "/12"

        return render(request, "userpanel/dashboard.html", {
            "email": user_obj.username,
            "password": user_obj.s_password,
            "type": type,
            "cur_month": today.month,
            "daily_chart_title": daily_chart_title,
            "monthly_chart_title": monthly_chart_title,
            "simcard_data": simcard_data,
            "page_text": page_text
        })

    except Exception as e:
        return render(request, "userpanel/dashboard.html", {
            "type": type,
            "cur_month": today.month,
            "daily_chart_title": daily_chart_title,
            "monthly_chart_title": monthly_chart_title,
            "simcard_data": {},
            "page_text": page_text
        })


# ***********************************************************************************
# @function: Update ICCID
# -----------------------------------------------------------------------------------
def updateIccid(request):
    try:
        iccid = request.POST["iccid"]
        status = request.POST["status"]
        res = updateSimStatus(iccid, status)
        if res == False:
            return HttpResponse("error", status=500)
        return HttpResponse("success")

    except Exception as e:
        return HttpResponse("error", status=500)