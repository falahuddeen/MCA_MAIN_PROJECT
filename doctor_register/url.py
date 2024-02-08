from django.conf.urls import url
from doctor_register import views

urlpatterns = [
    url('admin_manage_doctor/',views.admin_manage_doctor),
    url('view_approved_doctor/',views.admin_view_approved_doctor),
    url('doctor_register/',views.doctor_registration),
    url('doctor_profile_management/',views.doctor_profile_managment),
    url('user_view_doctor/',views.user_view_doctor)
]