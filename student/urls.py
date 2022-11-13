#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@software: PyCharm
@file: urls.py
@time: 2022/11/4 14:42
"""

from django.urls import path
from . import views

app_name = 'student'
urlpatterns = [
    path('students/', views.students, name='students'),
    path('add/', views.student_add, name="add"),
    path('delete/<pk>', views.student_delete, name="delete"),
    path('detail/<pk>', views.student_detail, name="detail"),
    path('edit/<pk>', views.student_edit, name="edit"),
    path('login/', views.login_view, name='student_login'),
    path('logout/', views.logout_view, name='student_logout'),
    path('register/', views.register, name='register'),
    path('detail_form_edit/<pk>', views.form_edit, name='detail_form_edit'),
    path('detail_form_add/', views.form_add, name='detail_form_add'),
]
