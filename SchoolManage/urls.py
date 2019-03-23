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
    url(r'^index/', views.school_manage_index),
]