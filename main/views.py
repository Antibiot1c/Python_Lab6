from django.shortcuts import render
from django.http import HttpResponse
from .models import Group, Student

def index(request):
    return HttpResponse("Welcome to the Educational Department!")

def groups(request):
    all_groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': all_groups})

def students(request):
    all_students = Student.objects.all()
    return render(request, 'students.html', {'students': all_students})

def group_detail(request, group_id):
    group = Group.objects.get(id=group_id)
    return render(request, 'group_detail.html', {'group': group})

def student_detail(request, student_id):
    student = Student.objects.get(id=student_id)
    return render(request, 'student_detail.html', {'student': student})
