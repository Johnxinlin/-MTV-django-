#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: views.py
@time: 2022/11/3 15:43
"""
from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, keso")

def detail(request, id):
    return HttpResponse(f"学生id为{id}")

def student_list(request, year, month):
    return HttpResponse(f"学生注册信息： 年：{year}, 月：{month}")