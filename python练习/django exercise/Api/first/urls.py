from django.urls import path
from .views import CourseCategoryView, CourseView

urlpatterns = [
    path('category/', CourseCategoryView.as_view()),
    path('', CourseView.as_view()),
]
