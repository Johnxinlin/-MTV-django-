#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@software: PyCharm
@file: middleware.py.py
@time: 2022/11/13 14:57
"""
from django.http import HttpResponseForbidden


def simple_middleware(get_response):
    # 一次性设置（初始化）
    print('初始化部分')

    def middleware(request):
        # 视图调用前
        print('处理请求之前执行的代码')
        user_agent = request.META.get('HTTP_USER_AGENT')
        if not 'chrome' in user_agent.lower():
            return HttpResponseForbidden()
        # 调用下一个中间件
        response = get_response(request)
        # 视图调用后
        print('响应之后的代码')
        return response

    return middleware


class SimpleMiddleWare:
    def __init__(self, get_response):
        self.get_response = get_response
        # 一次性设置（初始化）
        print('初始化部分')

    def __call__(self, request):
        # 视图调用前
        print('处理请求之前执行的代码')

        # 调用视图函数
        response = self.get_response(request)

        # 调用视图函数后
        print('响应之后的代码')

        return response
