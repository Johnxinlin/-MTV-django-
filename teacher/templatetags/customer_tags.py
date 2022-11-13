#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@software: PyCharm
@file: customer_tags.py
@time: 2022/11/7 14:20
"""

from django import template
from datetime import datetime

register = template.Library()


@register.simple_tag(takes_context=True)
def now_time(context):
    return datetime.now().strftime(context['format_str'])

@register.inclusion_tag('teacher/showList.html')
def show_list(value, style='link'):
    return {'ls': value, 'style': style}
