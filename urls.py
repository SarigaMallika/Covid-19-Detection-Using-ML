"""
FathimaPython URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/

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
from django.urls import path
from .covidapp import views
#from .covid19_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index),
    path('about/', views.about),
    path('user_reg/', views.user_reg),
    path('save_user/', views.save_user),
    path('med_reg/', views.med_reg),
    path('save_medical/', views.save_medical),
    path('user_login/', views.user_login),
    path('medical_login/', views.medical_login),
    path('admin_login/', views.admin_login),
    path('user_log/', views.user_log),
    path('user_logout/', views.user_logout),
    path('add_symptoms/', views.add_symptoms),
    path('save_symptoms/', views.save_symptoms),
    path('medical_log/', views.medical_log),
    path('med_logout/', views.med_logout),
    path('view_users/', views.view_users),
    path('view_symptoms/', views.view_symptoms),
    path('send_message/', views.send_message),
    path('save_message/', views.save_message),
    path('view_reply/', views.view_reply),
    path('admin_log/', views.admin_log),
    path('admin_logout/', views.admin_logout),
    path('all_users/', views.all_users),
    path('all_medicals/', views.all_medicals),
    path('all_result/', views.all_result),
    path('all_reply/', views.all_reply),
]
