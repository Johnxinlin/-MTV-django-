#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: customerFilters.py
@time: 2022/11/9 21:16
"""
from django import template

register = template.Library()

@register.filter()
def to_sex(value, arg='zh'):
    change = {
        'zh':('女', '男'),
        'en':('female', 'male'),
    }
    return change[arg][value]
