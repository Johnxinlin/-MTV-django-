#!/usr/bin/python3 
# encoding: utf-8 

"""
@version: v1.0
@author: ligui
@contact: 1947346653@qq.com
@site: https://www.cnblogs.com/c-x-a
@software: PyCharm
@file: customerTags.py
@time: 2022/11/9 21:16
"""
from django import template

from student.models import Grade

register = template.Library()


@register.inclusion_tag('student/show_class.html')
def show_class(student):
    '''
    下拉框模板标签
    :param student:
    :return: {'student':student, 'grades':grades}
    '''
    grades = Grade.objects.all()
    return {'student': student, 'grades': grades}


@register.inclusion_tag('student/paginator.html', takes_context=True)
def pagination_html(context):
    # page_list
    page = int(context['page'])
    total_page = context['total_page']
    per_page = context['per_page']
    num = 1  # 当前页左右各显示几页
    page_list = []

    # 1.当前页+左边页码列表
    # 1.1左边不够显示
    if page - num < 1:  # 页码范围1到当前页
        for i in range(1, page + 1):
            page_list.append(i)
    # 1.2 左边够显示，页码范围是page-num到当前页
    else:
        for i in range(page-num, page + 1):
            page_list.append(i)

    # 2.右边显示页码列表
    # 2.1右边够显示
    if page + num > total_page:
        for i in range(page + 1, total_page + 1):
            page_list.append(i)
    else:
        for i in range(page + 1, page + num + 1):
            page_list.append(i)

    return {
        'page_list': page_list,
        'page': page,
        'per_page':per_page,
        'total_page':total_page
    }

@register.simple_tag()
def add_class(field, class_str):
    return field.as_widget(attrs={'class': class_str})