from django.conf.urls import url
from appointment import views

urlpatterns=[
    url('appointment/',views.appointment),
    url('manage/',views.manage_appointment),
    url('approve/(?P<idd>\w+)',views.approve),
    url('reject/(?P<idd>\w+)',views.reject)
]