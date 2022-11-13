#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@software: PyCharm
@file: urls.py
@time: 2022/11/4 14:20
"""
from django.urls import path
from . import views

app_name = 'teacher'
urlpatterns = [
    path('index/', views.index, name='index'),
    path('students/', views.students, kwargs={'args': 'something'}),
    path('test/', views.students,kwargs={'args': 'something'}),
    path('login/', views.login),
    path('detail/<name>', views.detail, name="detail"),
    path('upload', views.upload_files, name="upload")
]