from django.core.exceptions import ValidationError
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from django.contrib import auth
from first.models import UserInfo
from django.forms import widgets
from django import forms
import re
import random


# Create your views here.
def enter(request):
    if request.is_ajax():
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        code = request.POST.get("code")
        response = {'user': None, 'err_msg': ""}
        if code.upper() == request.session.get("keep_str").upper():
            if auth.authenticate(username=user, password=pwd):
                response['user'] = user
            else:
                response['err_msg'] = "用户名或者密码错误"
        else:
            response['err_msg'] = "验证码错误"
        return JsonResponse(response)
    else:
        return render(request, "enter.html")


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def photo(request):
    img = Image.new("RGB", (200, 50), (random_color()))
    # f = open("static/img/valid.png", "wb")
    # img.save(f, "png")
    # with open("static/img/valid.png", "rb") as f:
    #     data = f.read()
    keep_str = ""
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype("static/font/kumo.ttf", 32)
    for i in range(0, 6):
        random_num = chr(random.randint(48, 57))
        random_upper = chr(random.randint(65, 90))
        random_lower = chr(random.randint(97, 122))
        random_char = random.choice([random_num, random_lower, random_upper])
        draw.text((i * 20 + 40, 0), random_char, (random_color()), font=font)
        keep_str += random_char
    print(keep_str)
    request.session['keep_str'] = keep_str
    f = BytesIO()
    img.save(f, "png")
    data = f.getvalue()
    return HttpResponse(data)


def register(request):
    if request.method == "GET":
        uf = UserForm()
        return render(request, "register.html", locals())
    if request.method == "POST":
        print(request.POST)
        uf = UserForm(request.POST)
        res = {"user": None, "err_msg": ""}
        if uf.is_valid():
            res["user"] = request.POST.get("user")
            print(uf.cleaned_data)
            user = uf.cleaned_data.get("user")
            pwd = uf.cleaned_data.get("pwd")
            email = uf.cleaned_data.get("email")
            UserInfo.objects.create_user(username=user, password=pwd, email=email)
        else:
            print(uf.errors)
            print(uf.cleaned_data)
            res["err_msg"] = uf.errors
        return JsonResponse(res)


class UserForm(forms.Form):
    user = forms.CharField(min_length=5,
                           widget=widgets.TextInput(attrs={"class": "form-control"}),
                           label="用户")
    gender = forms.ChoiceField(choices=((1, "男"), (2, "女")),
                               label="性别")
    pwd = forms.CharField(min_length=5,
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                          label="密码")
    r_pwd = forms.CharField(min_length=5,
                            widget=widgets.PasswordInput(attrs={"class": "form-control"}),
                            label="确认密码")
    email = forms.EmailField(min_length=5,
                             widget=widgets.TextInput(attrs={"class": "form-control"}),
                             label="邮箱")

    def clean_user(self):
        """判断用户名是否重复"""
        val = self.cleaned_data.get("user")
        user = UserInfo.objects.filter(username=val).first()
        if user:
            raise ValidationError("用户已经存在")
        else:
            return val

    def clean_pwd(self):
        """判断用户密码是否为纯数字"""
        val = self.cleaned_data.get("pwd")
        if val.isdigit():
            raise ValidationError("密码不能为纯数字")
        else:
            return val

    def clean(self):
        """判断两次输入的密码是否相同"""
        pwd = self.cleaned_data.get("pwd")
        r_pwd = self.cleaned_data.get("r_pwd")
        if pwd and r_pwd:
            if pwd == r_pwd:
                return self.cleaned_data
            else:
                self.add_error("r_pwd", ValidationError("两次密码不一致"))
        else:
            return self.cleaned_data

    def clean_email(self):
        """判断邮箱是否与QQ邮箱"""
        val = self.cleaned_data.get("email")
        if re.search("\w+@qq.com$", val):
            return val
        else:
            raise ValidationError("请使用QQ邮箱进行注册")
