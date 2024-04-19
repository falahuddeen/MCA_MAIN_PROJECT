from django.conf.urls import url
from appointment import views

urlpatterns=[
    url('appointment/(?P<idd>\w+)',views.appointment),
    url('manage/',views.manage_appointment),
    url('user_view_status/',views.user_view_status),
    url('schedule_time/(?P<idd>\w+)',views.schedule_time)
]