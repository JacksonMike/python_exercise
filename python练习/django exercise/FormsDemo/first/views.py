from django.shortcuts import render, HttpResponse
from django.core.exceptions import ValidationError
from django.forms import widgets
from first.models import UserInfo
from django import forms


# Create your views here.
def register(request):
    if request.method == "GET":
        form = UserForm()
        return render(request, "register.html", locals())
    else:
        print(request.POST)
        form = UserForm(request.POST)
        if form.is_valid():
            # 匹配成功的数据
            print(form.cleaned_data)
            UserInfo.objects.create(**form.cleaned_data)
            return HttpResponse("注册成功")
        else:
            # 未能匹配的数据
            error_data = form.errors
            return render(request, "register.html", locals())


class UserForm(forms.Form):
    user = forms.CharField(max_length=7,
                           label="用户名",
                           error_messages={"required": "该字段不能为空"},
                           widget=widgets.TextInput(attrs={"class": "form-control"}))
    pwd = forms.CharField(max_length=7,
                          label="密码",
                          error_messages={"required": "该字段不能为空"},
                          widget=widgets.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(min_length=5,
                             label="邮箱",
                             error_messages={"invalid": "邮箱格式错误", "required": "该字段不能为空"},
                             widget=widgets.EmailInput(attrs={"class": "form-control"}))

    def clean_user(self):
        """判断用户名是否被注册"""
        val = self.cleaned_data.get("user")
        if not UserInfo.objects.filter(user=val).first():
            return val
        else:
            raise ValidationError("该用户名已经被注册")

    def clean_pwd(self):
        val = self.cleaned_data.get("pwd")
        if val.isdigit():
            raise ValidationError("密码不能为纯数字")
        else:
            return val
