from django.conf.urls import url
from feedback import views

urlpatterns = [
    url('add_feedback/',views.add_feedback),
    url('view_feedback/',views.view_feedback)
]