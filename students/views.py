from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from students.models import ClassPage, AttendancePage

@login_required
def class_list(request):
    classes = ClassPage.objects.all()
    return render(request, 'students/class_list.html', {'classes':classes})

@login_required
def attendance_list(request):
    attendances = AttendancePage.objects.all()
    return render(request, 'students/attendance_list.html', {'attendances':attendances})