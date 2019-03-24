# !/usr/bin/python3
# coding=utf-8
# @Time    : 19-3-22 上午9:55
# @Author  : Paul
# @Email   : 287618817@qq.com
# @File    : urls.py
# @Software: PyCharm

from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.school_manage_index, name='index'), # 首页
    # 班级信息
    url(r'^add_class/$', views.school_manage_add_c, name='add_class'),  # 添加班级信息
    url(r'^display_class/$', views.school_manage_display_class, name='display_class'),  # 添加班级信息
    url(r'^del_class_info.html/$', views.school_manage_del_class_info, name='del_class_info.html'), # 删除班级信息
    url(r'^up_class_info.html/$', views.school_manage_up_class_info, name='up_class_info.html'),  # 更新班级信息
    # 学生信息
    url(r'^add_student/$', views.school_manage_add_student, name='add_student'),  # 添加学生信息
    url(r'^display_student/$', views.school_manage_display_student, name='display_student'), # 显示学生信息
    url(r'^delete_student.html/$', views.school_manage_delete_student, name='delete_student.html'),  # 删除学生信息
    url(r'^update_student.html/$', views.school_manage_update_student, name='update_student.html'),  # 更新学生信息

]