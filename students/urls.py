from django.conf.urls import url
from students import views

app_name='students'

urlpatterns = [
    url(r'^classes/$', views.class_list, name='class_list'),
    url(r'^attendances/$', views.attendance_list, name='attendance_list'),
]