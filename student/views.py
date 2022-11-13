from django.contrib.auth import authenticate, login, logout
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import render, reverse, redirect

from student.forms import StudentForm, StudentDetailForm, RegisterForm
from student.models import Student, Grade, StudentDetail
from django.contrib.auth.decorators import login_required, permission_required
from django.core.paginator import Paginator
import math


# Create your views here.
def students(request):
    section = "学生列表"
    search = request.GET.get('search')
    name = request.session.get('name')
    print(search)
    if search:
        search = search.strip()
        if search.isdigit():
            all_students = Student.objects.filter(Q(qq=search) | Q(phone=search), is_delete=False)
        else:
            all_students = Student.objects.filter(name=search, is_delete=False)
            print(all_students)
    else:
        all_students = Student.objects.filter(is_delete=False)

    all_students = all_students.order_by('-create_time')

    # 实现分页
    # 1.数据总数
    total_num = all_students.count()
    # 2.每页数据条数
    per_page = request.GET.get('per_page', 5)
    # 3.当前页码
    page = request.GET.get('page', 1)

    paginator = Paginator(all_students, per_page)

    all_students = paginator.get_page(page)

    return render(request, 'student/index.html', context={
        'section': section,
        'students': all_students,
        'page': page,
        'total_page': math.ceil(total_num / int(per_page)),
        'per_page': per_page,
        'name': name
    })


def student_add(request):
    if not request.user.has_perm('student.add_student'):
        return HttpResponse('你没有权限添加')
    section = "学生信息添加"
    if request.method == 'POST':
        try:
            message = request.POST
            data = {
                'name': message.get('username'),
                'age': message.get('age'),
                'qq': message.get('qq'),
                'sex': message.get('sex'),
                'phone': message.get('phone'),
                'grade_id': message.get('grade'),
            }
            num = message.get('num')
            college = message.get('college')
            s = Student.objects.create(**data)
            StudentDetail.objects.create(num=num, college=college, student=s)
            return redirect(reverse('student:students'))
        except Exception as e:
            return HttpResponse(e)
    # grades = Grade.objects.all()
    return render(request, 'student/detail.html', context={
        'section': section,
        # 'grades': grades
    })


def student_delete(request, pk):
    student = Student.objects.get(id=pk)
    student.is_delete = True
    student.save()
    return redirect(reverse('student:students'))


@login_required()
def student_detail(request, pk):
    # if not request.user.is_authenticated:
    #     return redirect(reverse('student:student_login') + f'?next={request.path}')
    section = "学生信息查询"
    student = Student.objects.get(id=pk)
    # grades = Grade.objects.all()
    return render(request, 'student/detail.html', context={
        'section': section,
        'student': student,
        # 'grades': grades
    })


def student_edit(request, pk):
    section = '学生信息编辑'
    # grades = Grade.objects.all()
    student = Student.objects.get(pk=pk)
    if request.method == 'POST':
        try:
            message = request.POST
            data = {
                'name': message.get('username'),
                'age': message.get('age'),
                'qq': message.get('qq'),
                'sex': message.get('sex'),
                'phone': message.get('phone'),
            }
            grade_id = message.get('grade')
            try:
                grade = Grade.objects.get(id=grade_id)
            except:
                grade = None
            try:
                s_detail = student.detail
            except:
                s_detail = StudentDetail()
                s_detail.student = student
            num = message.get('num')
            college = message.get('college')
            s_detail.num = num
            s_detail.college = college
            s_detail.save()
            Student.objects.filter(pk=pk).update(**data, grade=grade)
            return redirect(reverse('student:students'))
        except Exception as e:
            print(e)
            return HttpResponse(e)

    return render(request, 'student/detail.html', context={
        'section': section,
        # 'grades': grades,
        'student': student
    })


def form_edit(request, pk):
    student = Student.objects.get(pk=pk)
    section = '学生信息编辑'
    form = StudentForm(instance=student)
    detail_form = StudentDetailForm(instance=student.detail)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        try:
            detail_form = StudentDetailForm(request.POST, instance=student.detail)
        except:
            student_detail = StudentDetail()
            student_detail.student = student
            student_detail.save()
            detail_form = StudentDetailForm(request.POST, instance=student.detail)

        if form.is_valid() and detail_form.is_valid():
            form.save()
            detail_form.save()
            return redirect(reverse('student:students'))

    return render(request, 'student/form_detail.html', context={
        'form': form,
        'detail_form': detail_form,
        'section': section
    })


@permission_required('student.add_student', raise_exception=True)
def form_add(request):
    # if not request.user.has_perm('student.add_student'):
    #     return HttpResponse('你没有权限添加')
    section = '学生信息添加'
    form = StudentForm()
    detail_form = StudentDetailForm()

    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()

        student = Student.objects.last()
        # student = Student.objects.get(qq=form.cleaned_data.get('qq'))
        try:
            detail_form = StudentDetailForm(request.POST, instance=student.detail)
        except:
            student_detail = StudentDetail()
            student_detail.student = student
            student_detail.save()
            detail_form = StudentDetailForm(request.POST, instance=student.detail)

        if form.is_valid() and detail_form.is_valid():
            form.save()
            detail_form.save()
            return redirect(reverse('student:students'))

    return render(request, 'student/form_detail.html', context={
        'section': section,
        'form': form,
        'detail_form': detail_form
    })


# def login(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#
#         if username == 'feifei' and password == 'feifei':
#             # 将用户名保存到session
#             request.session['name'] = username
#             request.session.set_expiry(10)
#             return redirect(reverse('student:students'))
#     return render(request, 'student/login.html')

def login_view(request):
    next_url = request.GET.get('next')
    if request.user.is_authenticated:
        if next_url:
            return redirect(next_url)
        return redirect(reverse('student:students'))
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # 校验用户名和密码
        user = authenticate(username=username, password=password)
        if user:
            # 将用户名保存到session
            login(request, user)
            if next_url:
                return redirect(next_url)
            return redirect(reverse('student:students'))

    return render(request, 'student/login.html')


# def logout(request):
#     request.session.flush()
#     return redirect(reverse('student:students'))

def logout_view(request):
    logout(request)
    return redirect(reverse('student:students'))


def register(request):
    if request.method == 'GET':
        form = RegisterForm()
    elif request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            if password_repeat != password:
                return HttpResponse('注册成功')
    return render(request, 'student/register.html', context={
        'form': form
    })
