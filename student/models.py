from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField("学生姓名", max_length=20)
    age = models.SmallIntegerField("年龄")
    sex = models.SmallIntegerField(default=1)
    qq = models.CharField(max_length=20, unique=True, error_messages={'unique': 'qq号码已被使用'})
    phone = models.CharField(max_length=20, unique=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
    update_time = models.DateTimeField("修改时间", auto_now=True)
    grade = models.ForeignKey("Grade", on_delete=models.SET_NULL, null=True)
    is_delete = models.BooleanField(default=False)


class StudentDetail(models.Model):
    num = models.CharField('身份证', unique=True, max_length=40, default='')
    college = models.CharField('毕业学校', max_length=20, default='')
    student = models.OneToOneField('Student', related_name='detail', on_delete=models.CASCADE)


class Grade(models.Model):
    name = models.CharField('班级名称', max_length=20)
    num = models.CharField('班期', max_length=20)

    def __str__(self):
        return self.name + '-' + self.num


class Course(models.Model):
    name = models.CharField("课程名称", max_length=20)
    students = models.ManyToManyField('Student', through='Enroll')


class Enroll(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)
