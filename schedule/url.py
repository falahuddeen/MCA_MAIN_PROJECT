from django.conf.urls import url
from schedule import views

urlpatterns = [
    url('schedule_management/',views.schedule_management),
    url('schedule/',views.schedule),
    url('view/',views.view_schedule)
]