from django.shortcuts import render, HttpResponse, redirect
from rbac.service.rbac import initial_session
from first.models import *

# Create your views here.
def customer(request):
    return HttpResponse("customer")


def order(request):
    return HttpResponse("order")


def order_add(request):
    return HttpResponse("order_add")


def customer_add(request):
    return HttpResponse("customer_add")


def order_delete(request, pk):
    return HttpResponse("order_delete" + pk)


def customer_delete(request, pk):
    return HttpResponse("customer_delete" + pk)


def order_edit(request, pk):
    return HttpResponse("order_edit" + pk)


def customer_edit(request, pk):
    return HttpResponse("customer_edit" + pk)


def enter(request):
    if request.method == "GET":
        return render(request, "enter.html")
    else:
        name = request.POST.get("name")
        pwd = request.POST.get("pwd")
        user_obj = User.objects.filter(name=name, pwd=pwd).first()
        if user_obj:
            # 查询当前登录人的所有权限
            request.session["user_id"] = user_obj.pk
            # 将当前登陆人的权限录入session中
            initial_session(request, name)
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("用户名或者密码错误")
