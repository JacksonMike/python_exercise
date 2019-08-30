import uuid

from django.shortcuts import render
from rest_framework.response import Response

from .models import User
# Create your views here.
from rest_framework.views import APIView
from rest_framework import throttling
from .auth import MyAuth
from .permission import MyPermission
from .throttle import MyThrottle, DrfThrottle


class LoginView(APIView):
    def post(self, request):
        name = request.data.get("name", "")
        pwd = request.data.get("pwd", "")
        user_obj = User.objects.filter(name=name, pwd=pwd).first()
        if user_obj:
            user_obj.token = uuid.uuid4()
            user_obj.save()
            return Response(user_obj.token)
        else:
            return Response("用户名或者密码错误")


class TestView(APIView):
    authentication_classes = [MyAuth, ]

    def get(self, request):
        return Response("测试认证组件")


class TestPermissionView(APIView):
    authentication_classes = [MyAuth, ]
    permission_classes = [MyPermission, ]
    throttle_classes = [DrfThrottle, ]

    def get(self, request):
        return Response("只有VIP用户才能看电影")
