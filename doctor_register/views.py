from django.shortcuts import render
from doctor_register.models import DoctorRegister
# Create your views here.

def admin_manage_doctor(request):
    obj=DoctorRegister.objects.all()
    data={
        'x':obj
    }
    return render(request,'doctor_register/Admin_Manage_Doctor.html',data)

def approve(request,idd):
    obj=DoctorRegister.objects.get(doctor_id=idd)
    obj.status='Approved'
    obj.save()
    return admin_manage_doctor(request)

def reject(request,idd):
    obj=DoctorRegister.objects.get(doctor_id=idd)
    obj.status='Rejected'
    obj.save()
    return admin_manage_doctor(request)

def admin_view_approved_doctor(request):
    obj = DoctorRegister.objects.filter(status='Approved')
    data = {
        'x': obj
    }
    return render(request,'doctor_register/Admin_View_Approved_Doctor.html',data)

def doctor_registration(request):
    if request.method=='POST':
        obj=DoctorRegister()
        obj.name=request.POST.get('dname')
        obj.mobile=request.POST.get('dmobile')
        obj.email=request.POST.get('dmail')
        obj.age=request.POST.get('dmobile')
        obj.gender=request.POST.get('Gender')
        obj.qualification=request.POST.get('file')
        obj.specialization=request.POST.get('specialization')
        obj.profile_pic=request.POST.get('profile_pic')
        obj.password=request.POST.get('dpass')
        obj.save()
    return render(request,'doctor_register/Doctor_Registration.html')

def doctor_profile_managment(request):
    obj = DoctorRegister.objects.all()
    data = {
        'x': obj
    }
    return render(request,'doctor_register/Doctor_View_Profile_and_Manage.html',data)

def doctor_update(request,idd):
    obj = DoctorRegister.objects.get(doctor_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=DoctorRegister.objects.get(doctor_id=idd)
        obj.name=request.POST.get('dname')
        obj.mobile=request.POST.get('dmobile')
        obj.email=request.POST.get('dmail')
        obj.age=request.POST.get('dmobile')
        obj.gender=request.POST.get('Gender')
        obj.qualification=request.POST.get('file')
        obj.specialization=request.POST.get('specialization')
        obj.profile_pic=request.POST.get('profile_pic')
        obj.password=request.POST.get('dpass')
        obj.save()
        return doctor_profile_managment(request)
    return render(request, 'doctor_register/Doctor_Profile_Update.html', context)

def user_view_doctor(request):
    obj = DoctorRegister.objects.all()
    data= {
        'x': obj
    }
    return render(request,'doctor_register/User_View_Doctors.html',data)