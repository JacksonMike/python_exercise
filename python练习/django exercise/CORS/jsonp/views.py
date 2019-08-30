from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView


class CorsDemoView(APIView):
    def get(self, request):
        return HttpResponse("get ok")

    def post(self, request):
        return HttpResponse("post ok")

    def put(self, request):
        return HttpResponse("put ok")
