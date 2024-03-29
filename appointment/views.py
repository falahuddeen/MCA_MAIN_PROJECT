from macpath import split

from django.shortcuts import render
from appointment.models import Appointment
from doctor_register.models import DoctorRegister
from schedule.models import Schedule
from datetime import datetime

# Create your views here.

def appointment(request,idd):
    obk=Schedule.objects.get(schedule_id=idd)
    context={
        'a':obk
    }
    if request.method=='POST':
        obj=Appointment()
        uid=request.session["u_id"]
        obj.user_id=uid
        # obj.doctor_id=request.POST.get('dname')
        obj.schedule_id=idd
        obj.date=request.POST.get('date')
        obj.time='00:00:00'
        obj.status='Time Not Scheduled'
        obj.save()
    return render(request,'appointment/Appointment.html',context)


def manage_appointment(request):
    uid=request.session["u_id"]
    obj=Appointment.objects.filter(schedule__doctor_id=uid)
    context={
        'x':obj
    }
    return render(request,'appointment/Doctor_Manage_Patient_Appointment.html',context)


# def approve(request,idd): removed method
#     obj=Appointment.objects.get(appointment_id=idd)
#     obj.status='Approved'
#     obj.save()
#     return manage_appointment(request)

def schedule_time(request,idd):
    obj=Appointment.objects.get(appointment_id=idd)
    context={
        'x':obj,
    }
    dateconvert=split(str(obj.date))
    c={
        "date":dateconvert[1]
    }
    if request.method=="POST":
        obj=Appointment.objects.get(appointment_id=idd)
        obj.status='Time Scheduled'
        obj.time=request.POST.get('time')
        obj.save()
    return render(request, 'appointment/Schedule_Time.html',c)

# def reject(request,idd):
#     obj=Appointment.objects.get(appointment_id=idd)
#     obj.status='Rejected'
#     obj.save()
#     return manage_appointment(request)

def user_view_status(request):
    uid=request.session["u_id"]
    obj=Appointment.objects.filter(user_id=uid)
    context={
        'x':obj
    }
    return render(request,'appointment/User_View_Appointment_Status.html',context)


