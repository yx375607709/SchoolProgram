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
    url(r'^index/$', views.school_manage_index), # 首页
    # 班级信息
    url(r'^index/add_class/$', views.school_manage_add_c),  # 添加班级信息
    url(r'^index/del_class_info.html/$', views.school_manage_del_class_info), # 删除班级信息
    url(r'^index/up_class_info.html/$', views.school_manage_up_class_info),  # 更新班级信息
    # 学生信息
    url(r'^index/display_student/add_student/$', views.school_manage_add_student),  # 添加班级信息
    url(r'^index/display_student/$', views.school_manage_display_student), # 删除班级信息
    url(r'^index/display_student/delete_student.html/$', views.school_manage_delete_student),  # 更新班级信息
    url(r'^index/display_student/update_student.html/$', views.school_manage_update_student),  # 更新班级信息

]