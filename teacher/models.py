from django.db import models


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=20, verbose_name="学生姓名", unique=True)  # 学生姓名
    age = models.SmallIntegerField(null=True)
    sex = models.SmallIntegerField(default=1)  # 设置默认值
    qq = models.CharField(max_length=20, null=True)
    phone = models.CharField(max_length=20, verbose_name="电话", null=True)
    create_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")  # 创建时间
    update_time = models.DateTimeField(auto_now=True, verbose_name="更新时间")
    # detail = models.OneToOneField('StudentDetail', on_delete=models.SET_NULL, null=True)  # 一对一对应学生详情表，设置为空删除
    grade = models.ForeignKey('Grade', on_delete=models.SET_NULL, null=True, related_name='student')

    def __str__(self):
        return self.name

    # class Meta:
    #     db_table = "student"


class StudentDetail(models.Model):
    college = models.CharField(verbose_name="学院名", max_length=20, default='')
    student = models.OneToOneField('Student', on_delete=models.CASCADE)

    def __str__(self):
        return self.college


class Grade(models.Model):
    name = models.CharField(verbose_name="班级名称", max_length=20)
    num = models.CharField(verbose_name='班期', max_length=20)

    def __str__(self):
        return self.name + '-' + self.num


class Course(models.Model):
    name = models.CharField(verbose_name="课程名称", max_length=20)
    students = models.ManyToManyField('Student', through='Enroll')

    def __str__(self):
        return self.name

class Enroll(models.Model):
    student = models.ForeignKey('Student', on_delete=models.CASCADE)
    course = models.ForeignKey('Course', on_delete=models.CASCADE)
    c_time = models.DateTimeField('选课时间', auto_now_add=True)