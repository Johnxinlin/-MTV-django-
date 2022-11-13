import os
from datetime import datetime

from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django.template.loader import get_template

from ClientSystem.settings import MEDIA_ROOT
from .models import Student
from datetime import datetime


# Create your views here.

def index(request):
    """
    t = get_template('teacher/index.html')
    html = t.render()
    return HttpResponse(html)
    """
    students = Student.objects.all()
    num = request.COOKIES.get('num')
    if num:
        num = 1 + int(num)
    else:
        num = 1
    lt = [1, 2, 3]
    dt = {'name': "钟灵珠", 'age': 18, 'sex': 0}
    # students = [
    #     {'name': "钟灵珠", 'age': 19, 'sex': 1, 'id': 0, 'course': ['python', 'English', 'java', 'Sport']},
    #     {'name': "的说法", 'age': 185, 'sex': 0, 'id': 1, 'course': ['python', 'English', 'java', 'Sport']},
    #     {'name': "范德萨个", 'age': 138, 'sex': 1, 'id': 2, 'course': ['python', 'English', 'java', 'Sport']},
    #     {'name': "的撒个", 'age': 182, 'sex': 0, 'id': 3, 'course': ['python', 'English', 'java', 'Sport']},
    # ]
    now = datetime.now()
    # now = now.strftime("%Y年%m月%d日  %H:%M:%S")
    js = '<script>alert("跨域脚本攻击")</script>'

    def func():
        return "something"

    response = render(request, 'teacher/index.html', context={
        'now': now,
        'lt': lt,
        'dt': dt,
        'func': func,
        'js': js,
        'students': students,
        'format_str': '%Y年%m月%d日  %H:%M:%S',
        'num': num
    })
    response.set_cookie('num', num)
    return response
    # return render(request, 'teacher/index_new.html')


def students(request, args):
    return HttpResponse(f"额外参数{args}")


def test(request, args):
    return HttpResponse(f"额外参数{args}")


def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        return redirect('teacher:index')
    return render(request, 'teacher/login.html')


def detail(request, name):
    return HttpResponse(f'这是{name}同学的详情')

def upload_files(request):
    if request.method == "POST":
        files = request.FILES.getlist('file')

        # 保存文件
        # 每天上传的文件放入每天的文件夹
        day_dir_name = datetime.now().strftime('%Y-%m-%d')
        day_dir = os.path.join(MEDIA_ROOT, day_dir_name)
        if not os.path.exists(day_dir):
            os.mkdir(day_dir)

        # 保存文件
        for file in files:
            filename = os.path.join(day_dir, file.name)
            with open(filename, 'wb') as  fb:
                for line in file.chunks():  # 上传文件时，会自动分块
                    fb.write(line)
    return render(request, 'teacher/upload.html')

