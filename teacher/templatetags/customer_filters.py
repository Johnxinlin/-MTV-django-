#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: customer_filters.py
@time: 2022/11/7 14:18
"""
from django import template

register = template.Library()  # 此处变量名必须为register否则报错


@register.filter(name='to_sex')
def to_sex(value, arg='zh'):
    change = {
        'zh': ('女', '男'),
        'en': ('female', 'male')
    }
    return change[arg][value]
