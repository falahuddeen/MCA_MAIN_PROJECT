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
        obj.user_id=1
        obj.doctor_id=request.POST.get('dname')
        obj.schedule_id=idd
        obj.date=request.POST.get('date')
        obj.time=request.POST.get('time')
        obj.status='pending'
        obj.save()
    return render(request,'appointment/Appointment.html',context)


def manage_appointment(request):
    obj=Appointment.objects.all()
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
    #need session data
    obj=Appointment.objects.all()
    return render(request,'appointment/User_View_Appointment_Status.html')


