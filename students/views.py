from django.shortcuts import render
from students.models import ClassPage, AttendancePage

def class_list(request):
    classes = ClassPage.objects.all()
    return render(request, 'students/class_list.html', {'classes':classes})


def attendance_list(request):
    attendances = AttendancePage.objects.all()
    return render(request, 'students/attendance_list.html', {'attendances':attendances})