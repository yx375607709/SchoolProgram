
from django.db import models

# Create your models here.

class Classes(models.Model):
    '''
    班级表
    '''
    class_name = models.CharField('班级名称', max_length=32)
    class_type = models.CharField('年级名称', max_length=32, default='高中')
    # 指定多对多关系
    m = models.ManyToManyField('Teacher')

class Teacher(models.Model):
    '''
    老师表
    '''
    teacher_name = models.CharField('姓名', max_length=32)

class Student(models.Model):
    '''
    学生表
    '''
    student_name = models.CharField('姓名', max_length=32)
    # age = models.IntegerField('年龄')
    gender = models.NullBooleanField('性别')
    student_tel = models.CharField('学生电话', max_length=15)
    register_date = models.DateField('注册时间')
    student_type = models.CharField('生源类型', max_length=10)
    id_card = models.CharField('身份证', max_length=18)
    location_of_household_registration = models.CharField('户口性质', max_length=128)
    tel_two = models.CharField('第二联系人', max_length=15)
    major = models.CharField('专业', max_length=32)
    address = models.CharField('现居住地', max_length=128)
    status = models.CharField('学生状态', max_length=12)
    market = models.CharField('备注', max_length=1024)


