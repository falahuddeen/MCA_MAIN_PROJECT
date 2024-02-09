from django.conf.urls import url
from disease import views

urlpatterns = [
    url('add_disease/',views.add_disease),
    url('admin_manage_disease/',views.admin_manage_disease),
    url('doctor_manage_disease/',views.doctor_manage_disease),
    url('admin_update/(?P<idd>\w+)',views.admin_update),
    url('admin_delete/(?P<idd>\w+)',views.admin_delete),
    url('doctor_update/(?P<idd>\w+)',views.doctor_update),
    url('doctor_delete/(?P<idd>\w+)',views.doctor_delete)
]