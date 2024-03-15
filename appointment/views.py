from django.shortcuts import render
from appointment.models import Appointment
from doctor_register.models import DoctorRegister

# Create your views here.

def appointment(request,idd):
    obk=DoctorRegister.objects.all()
    context={
        'a':obk
    }
    if request.method=='POST':
        obj=Appointment()
        uid=request.session["u_id"]
        obj.user_id=uid
        obj.doctor_id=request.POST.get('dname')
        obj.schedule_id=idd
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.status='pending'
        obj.save()
    return render(request,'appointment/Appointment.html',context)


def manage_appointment(request):
    uid=request.session["u_id"]
    obj=Appointment.objects.filter(doctor_id=uid)
    context={
        'x':obj
    }
    return render(request,'appointment/Doctor_Manage_Patient_Appointment.html',context)


def approve(request,idd):
    obj=Appointment.objects.get(appointment_id=idd)
    obj.status='Approved'
    obj.save()
    return manage_appointment(request)

def reject(request,idd):
    obj=Appointment.objects.get(appointment_id=idd)
    obj.status='Rejected'
    obj.save()
    return manage_appointment(request)

def user_view_status(request):
    uid=request.session["u_id"]
    obj=Appointment.objects.filter(user_id=uid)
    context={
        'x':obj
    }
    return render(request,'appointment/User_View_Appointment_Status.html',context)


