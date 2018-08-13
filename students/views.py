from django.shortcuts import render
from students.models import ClassPage

def class_list(request):
    classes = ClassPage.objects.all()
    return render(request, 'students/class_list.html', {'classes':classes})
