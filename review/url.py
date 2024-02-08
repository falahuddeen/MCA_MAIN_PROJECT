from django.conf.urls import url
from review import views

urlpatterns = [
    url('add_review/',views.add_review),
    url('admin_view_doctor_review/',views.admin_view_doctor_review),
    url('doctor_view_review/',views.doctor_view_review)
]