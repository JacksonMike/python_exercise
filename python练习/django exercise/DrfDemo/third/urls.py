from django.contrib import admin
from django.urls import path, include
from .views import VersionDemo

urlpatterns = [
    path('version/', VersionDemo.as_view())
]
