"""Crm URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from first import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('enter/', views.enter),
    path('leave/', views.leave),
    path('get_img/', views.get_img),
    path('register/', views.register),
    path('index/', views.index),
    path('', views.index),
    path('customers_list/', views.CustomerView.as_view(), name="customers_list"),
    path('customers_public/', views.CustomerView.as_view(), name="customers_public"),
    path('my_customers/', views.CustomerView.as_view(), name="my_customers"),
    path('customers_add/', views.CustomerViewAddEdit.as_view(), name="customers_add"),
    re_path('customers_edit/(\d+)', views.CustomerViewAddEdit.as_view(), name="customers_edit"),
    path('consult_records/', views.ConsultRecordView.as_view(), name="consult_records"),
    path('consult_records_add/', views.ConsultRecordAddEdit.as_view(), name="consult_records_add"),
    re_path('consult_records_edit/(\d+)', views.ConsultRecordAddEdit.as_view(), name="consult_records_edit"),
    path('class_study_record/', views.ClassStudyRecordView.as_view(), name="class_study_record"),
    re_path('record_score/(\d+)', views.RecordScoreView.as_view(), name="record_score"),
    path('customers_statistics/', views.StatisticsView.as_view(), name="customers_statistics")
]
