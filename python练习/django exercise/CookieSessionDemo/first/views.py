from django.shortcuts import render, redirect, HttpResponse
from first.models import UserInfo
import datetime


# Create your views here.
def enter(request):
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if UserInfo.objects.filter(user=user, pwd=pwd):
            obj = redirect("/index/")
            # 设置cookie
            obj.set_cookie("user", user)
            obj.set_cookie("is_login", True, max_age=3600 * 24 * 7)
            return obj
        else:
            return HttpResponse("用户名或者密码错误")


def index(request):
    # 获取cookie
    print(request.COOKIES)
    is_login = request.COOKIES.get("is_login")
    user = request.COOKIES.get("user")
    if not is_login:
        return redirect("/enter/")
    return render(request, "index.html", {"user": user})


def session_enter(request):
    """
    if request.COOKIE.get("sessionid"):
               random_str=request.COOKIE.get("sessionid")
               在django-seesion表中过滤session-key=random_str的记录进行update
           else:
               1 生成一个随机字符串   23423hkjsf890234sd
               2 向django-session表中插入记录
                   session-key         session-data
                  23423hkjsf890234sd   {"susername":"egon","slogin":True}
               3 响应set_cookie :   {"sessionid":23423hkjsf890234sd}
    :param request:
    :return:
    """
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        if UserInfo.objects.filter(user=user, pwd=pwd):
            request.session["session_user"] = user
            request.session["session_login"] = True
            return redirect("/index_session/")
        else:
            return HttpResponse("用户名或者密码错误")


def index_session(request):
    """
    request.session
       1 request.COOKIE.get("sessionid")   :23423hkjsf890234sd
       2 在django-session表过滤session-key=23423hkjsf890234sd的记录
       3 取过滤记录的session-data反序列化成数据字典：{"susername":"egon","slogin":True}
    :param request:
    :return:
    """
    print(request.session)
    session_login = request.session.get("session_login")
    session_user = request.session.get("session_user")
    if not session_login:
        return redirect("/session_enter/")
    return render(request, "index_session.html", {"session_user": session_user})


def session_leave(request):
    request.session.flush()
    return redirect("/session_enter/")


def leave(request):
    obj = redirect("/index/")
    obj.delete_cookie("user")
    obj.delete_cookie("is_login")
    return obj
