from django.contrib.contenttypes.models import ContentType
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from .models import *


class TestView(APIView):
    def get(self, request):
        # content_type_obj = ContentType.objects.filter(app_label="first", model="meat").first()
        # print(type(content_type_obj))
        # model_class = content_type_obj.model_class()
        # print(model_class)
        # print(content_type_obj.pk)

        # 通过对象添加
        # meat_obj = Meat.objects.filter(pk=1).first()
        # Coupon.objects.create(title="8折", content_object=meat_obj)

        # 也可以直接添加
        # Coupon.objects.create(title="9折", content_type_id=9, object_id=2)

        # coupon_obj = Coupon.objects.filter(pk=8).first()
        # print(coupon_obj.content_object.name)

        meat_obj = Meat.objects.filter(pk=1).first()
        print(meat_obj.coupons.all())
        return HttpResponse("OK")
