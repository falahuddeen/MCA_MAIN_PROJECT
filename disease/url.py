from django.conf.urls import url
from disease import views

urlpatterns = [
    url('add_disease/',views.add_disease),
    url('admin_manage_disease/',views.admin_manage_disease),
    url('doctor_manage_disease/',views.doctor_manage_disease)
]