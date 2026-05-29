from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, redirect
from .db2 import check_login


def login_view(request):
    error = None

    if request.method == "POST":
        userid = request.POST.get("userid")
        password = request.POST.get("password")

        if check_login(userid, password):
            request.session["USERID"] = userid
            return redirect("mainpage")
        else:
            error = "Sai USERID hoặc PASSWD"

    return render(request, "accounts/login.html", {"error": error})


def mainpage_view(request):
    userid = request.session.get("USERID")

    if not userid:
        return redirect("login")

    return render(request, "accounts/mainpage.html", {"userid": userid})


def logout_view(request):
    request.session.flush()
    return redirect("login")