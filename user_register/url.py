from django.conf.urls import url
from user_register import views

urlpatterns = [
    url('admin_view_user/',views.admin_view_user),
    url('user_registration/',views.user_registration),
    url('user_view_profile/',views.user_view_profile)
]