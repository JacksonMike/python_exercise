from django.shortcuts import render

# Create your views here.
from rest_framework import versioning
from rest_framework.response import Response
from rest_framework.views import APIView


class VersionDemo(APIView):
    def get(self, request):
        print(request.version)
        print(request.versioning_scheme)
        if request.version == "v1":
            return Response("v1版本信息")
        return Response("没有该版本")
