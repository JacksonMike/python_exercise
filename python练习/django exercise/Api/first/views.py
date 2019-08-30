from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from . import models
from . import serializers


class CourseCategoryView(APIView):
    def get(self, request):
        queryset = models.Category.objects.all()
        ser_obj = serializers.CategorySerializer(queryset, many=True)
        return Response(ser_obj.data)


class CourseView(APIView):
    def get(self, request):
        category_id = request.query_params.get("category_id", "")
        if not category_id:
            queryset = models.Course.objects.all().order_by("order")
        else:
            queryset = models.Course.objects.filter(category_id=category_id)
        ser_obj = serializers.CourseSerializer(queryset, many=True)
        return Response(ser_obj.data)
