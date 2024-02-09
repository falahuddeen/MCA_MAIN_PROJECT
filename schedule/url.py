from django.conf.urls import url
from schedule import views

urlpatterns = [
    url('schedule_management/',views.schedule_management),
    url('schedule/',views.schedule),
    url('view/',views.view_schedule),
    url('doctor_schedule_update/(?P<idd>\w+)',views.doctor_schedule_update),
    url('doctor_schedule_delete/(?P<idd>\w+)',views.doctor_schedule_delete)
]