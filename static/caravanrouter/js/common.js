// *************** show message *************** //
function showMessage(type, title, msg, delay) {
	Lobibox.notify(type, {
		delay: delay,
		title: title.toUpperCase(),
		msg: msg
	});
}

// *************** convert month to string *************** //
function getMonthString(month) {
    var month_ary = ["January", "Feburary", "March", "April", "May", "Jun", "July", "August", "September",
            "October", "November", "December"];
    if (month >= 1 && month <= 12)
        return month_ary[month-1];
    return "";
}


// *************** alert list *************** //
var alert_list = new Array();

// *************** 0x1....  Admin Panel *************** //
alert_list["0x10001"] = {
    "mode": "warning",
    "title": "Warning",
    "msg": "Please enter all information"
};

alert_list["0x10002"] = {
    "mode": "warning",
    "title": "Warning",
    "msg": "Type User does not allowed to register morethan 2 sim cards"
};

alert_list["0x10003"] = {
    "mode": "warning",
    "title": "Success",
    "msg": "User has been registered"
};

alert_list["0x10004"] = {
    "mode": "warning",
    "title": "Warning",
    "msg": "Email is already registered"
};

alert_list["0x10005"] = {
    "mode": "warning",
    "title": "Warning",
    "msg": "Consumer Id is already registered"
};

alert_list["0x10006"] = {
    "mode": "warning",
    "title": "Error",
    "msg": "Sorry, something went wrong while registering user"
};

alert_list["0x10007"] = {
    "mode": "warning",
    "title": "Success",
    "msg": "User has been updated"
};

alert_list["0x10008"] = {
    "mode": "warning",
    "title": "Error",
    "msg": "Sorry, something went wrong while updating user"
};

alert_list["0x10009"] = {
    "mode": "warning",
    "title": "Success",
    "msg": "User has been deleted"
};

alert_list["0x1000A"] = {
    "mode": "warning",
    "title": "Error",
    "msg": "Sorry, something went wrong while deleting user"
};
