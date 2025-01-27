"""brain_tumour URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import path,include
from temp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    url('appointment/',include('appointment.url')),
    url('chat/', include('chat.url')),
    url('disease/', include('disease.url')),
    url('doctor_register/', include('doctor_register.url')),
    url('feedback/', include('feedback.url')),
    url('login/', include('login.url')),
    url('review/', include('review.url')),
    url('schedule/', include('schedule.url')),
    url('user_register/', include('user_register.url')),
    url('temp/', include('temp.url')),
    url('predict/', include('predict.url')),
    url('$',views.home)

]
