from django.shortcuts import render
from students.models import StudentsProfilesIndexPage

def class_list(request):
    classes = StudentsProfilesIndexPage.objects.all()
    return render(request, 'students/class_list.html', {'classes':classes})
