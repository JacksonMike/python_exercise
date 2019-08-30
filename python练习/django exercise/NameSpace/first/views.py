from django.shortcuts import render, HttpResponse,redirect
from django.urls import reverse


# Create your views here.
def index(request):
    return redirect(reverse("two:index"))
