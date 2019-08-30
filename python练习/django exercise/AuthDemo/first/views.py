from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User


# Create your views here.

def enter(request):
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        obj = auth.authenticate(username=username, password=password)
        if obj:
            # request.session["user_id"]=user_obj.pk request.user：全局变量，模板，视图直接可以使用
            auth.login(request, obj)
            return redirect("/index/")
        else:
            return redirect("/enter/")


def index(request):
    print(request.user.is_active)
    username = request.user.username
    # 判断是否为匿名用户
    if request.user.is_active:
        return render(request, "index.html", locals())
    else:
        return redirect("/enter/")


def leave(request):
    auth.logout(request)
    return redirect("/index/")


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    else:
        username = request.POST.get("username")
        password = request.POST.get("password")
        # 创建用户
        User.objects.create_user(username=username, password=password)
        return redirect("/enter/")


def set_password(request):
    user = User.objects.get(username=request.user.username)
    user.set_password(raw_password=999)
    user.save()
    return redirect("/enter/")
