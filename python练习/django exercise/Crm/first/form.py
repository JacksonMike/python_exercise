from django.core.exceptions import ValidationError
from multiselectfield.forms.fields import MultiSelectFormField
from first.models import *
from django import forms
import re


class UserForm(forms.Form):
    """form组件认证"""
    user = forms.CharField(max_length=7, label="用户名")
    gender = forms.ChoiceField(choices=((1, "男"), (2, "女")), label="性别")
    pwd = forms.CharField(max_length=7, label="密码")
    ensure_pwd = forms.CharField(max_length=7, label="确认密码", )
    email = forms.EmailField(max_length=10, label="邮箱")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for filed in self.fields.values():
            filed.widget.attrs.update({'class': 'form-control'})

    def clean_user(self):
        """验证用户名是否重复"""
        val = self.cleaned_data.get("user")
        if UserInfo.objects.filter(username=val).first():
            raise ValidationError("用户名已经被注册")
        else:
            return val

    def clean_pwd(self):
        """验证密码是否为纯数字"""
        val = self.cleaned_data.get("pwd")
        if val.isdigit():
            raise ValidationError("密码为纯数字")
        else:
            return val

    def clean_ensure_pwd(self):
        val = self.cleaned_data.get("ensure_pwd")
        if val.isdigit():
            raise ValidationError("密码为纯数字")
        else:
            return val

    def clean_email(self):
        """判断是否为QQ邮箱"""
        val = self.cleaned_data.get("email")
        if re.search("\d+@qq.com", val):
            return val
        else:
            raise ValidationError("请使用QQ邮箱进行注册")

    def clean(self):
        """判断两次输入的密码是否一致"""
        pwd = self.cleaned_data.get("pwd")
        ensure_pwd = self.cleaned_data.get("ensure_pwd")
        if pwd and ensure_pwd and pwd == ensure_pwd:
            return self.cleaned_data
        else:
            self.add_error("ensure_pwd", ValidationError("两次密码不一致"))


class CustomerModelForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            if not isinstance(field, MultiSelectFormField):
                field.widget.attrs.update({"class": "form-control"})


class ConsultRecordModelForm(forms.ModelForm):
    class Meta:
        model = ConsultRecord
        exclude = ["delete_status"]


class StudentStudyRecordModelForm(forms.ModelForm):
    class Meta:
        model = StudentStudyRecord
        fields = ["score", "homework_note"]
