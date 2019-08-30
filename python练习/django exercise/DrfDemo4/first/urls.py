from .views import LoginView, TestView, TestPermissionView
from django.urls import path

urlpatterns = [
    path('login/', LoginView.as_view()),
    path('test/', TestView.as_view()),
    path('permission/', TestPermissionView.as_view()),
]
