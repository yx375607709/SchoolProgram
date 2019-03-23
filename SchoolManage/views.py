from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import *


# Create your views here.

# 管理页面首页
def school_manage_index(request):
    obj = Classes.objects.all()
    return render(request, "school_manage_index.html", locals())

# ---------------------------------    班级管理页面   --------------------------------------

# 添加班级信息
def school_manage_add_c(request):
    if request.method == 'GET':
        return render(request, 'school_manage_add_class.html')
    elif request.method == 'POST':
        class_name = request.POST.get('class_name')
        class_type = request.POST.get('class_type')
        Classes.objects.create(class_name=class_name, class_type=class_type)
        return HttpResponseRedirect('/schoolmanage/index')

# 删除班级信息
def school_manage_del_class_info(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        Classes.objects.filter(id=cid).delete()
        return HttpResponseRedirect('/schoolmanage/index')

#更新班级信息
def school_manage_up_class_info(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        obj = Classes.objects.filter(id=cid)
        return render(request, 'school_manage_up_class.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.POST.get('cid')
        class_name = request.POST.get('class_name')
        class_type = request.POST.get('class_type')
        Classes.objects.filter(id=cid).update(class_name=class_name, class_type=class_type)
        return HttpResponseRedirect('/schoolmanage/index')

# ---------------------------------    学生信息页面   --------------------------------------

def school_manage_add_student(request):
    if request.method == 'GET':
        return render(request, 'school_manage_add_student.html')
    elif request.method == 'POST':
        student_name = request.POST.get('student_name')
        # age = models.IntegerField('年龄')
        gender = request.POST.get('gender')
        student_tel = request.POST.get('student_tel')
        register_date = request.POST.get('register_date')
        student_type = request.POST.get('student_type')
        id_card = request.POST.get('id_card')
        location_of_household_registration = request.POST.get('location_of_household_registration')
        tel_two = request.POST.get('tel_two')
        major = request.POST.get('major')
        address = request.POST.get('address')
        status = request.POST.get('status')
        market = request.POST.get('market')

        Student.objects.create(
            student_name=student_name,
            gender = gender,
            student_tel = student_tel,
            register_date = register_date,
            student_type = student_type,
            id_card = id_card,
            location_of_household_registration = location_of_household_registration,
            tel_two = tel_two,
            major = major,
            address = address,
            status = status,
            market = market,
            )

        sbm = request.POST.get('sbm')
        if sbm == '下一个':
            return HttpResponseRedirect('/schoolmanage/index/display_student/add_student/')
        elif sbm == '提交保存':
            return HttpResponseRedirect('/schoolmanage/index/display_student')

def school_manage_display_student(request):
    obj = Student.objects.all()
    return render(request, "school_manage_display_student.html", locals())

def school_manage_delete_student(request):
    if request.method =='GET':
        cid = request.GET.get("cid")
        Student.objects.filter(id__exact=cid).delete()
        return HttpResponseRedirect('/schoolmanage/index/display_student')

def school_manage_update_student(request):
    if request.method == 'GET':
        cid = request.GET.get('cid')
        obj = Classes.objects.filter(id=cid)
        return render(request, 'school_manage_up_student.html', {'obj': obj})
    elif request.method == 'POST':
        cid = request.POST.get('cid')
        class_name = request.POST.get('class_name')
        class_type = request.POST.get('class_type')
        Classes.objects.filter(id=cid).update(class_name=class_name, class_type=class_type)
        return HttpResponseRedirect('/schoolmanage/index/display_student')