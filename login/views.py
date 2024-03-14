from django.shortcuts import render
from login.models import Login
from doctor_register.models import DoctorRegister
from user_register.models import UserRegister
from django.http import HttpResponseRedirect
# Create your views here.



def login(request):
    if request.method == "POST":
        name=request.POST.get("username")
        password=request.POST.get("pass")
        obj=Login.objects.filter(username=name,password=password)
        tp=""
        for ob in obj:
            tp=ob.type
            uid=ob.uid
            if tp=="admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "doctor":
                ob=DoctorRegister.objects.get(doctor_id=uid)
                if ob.status=="Approved":
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/doctor/')
                else:
                    message="Your Registration is Pending.."
                    context={
                        'msg':message,
                    }
                    return render(request,'login/Login.html',context)
            elif tp == "user":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/user/')
        else:
            objilist="Incorrect Username or Password ... Please try again..!"
            context={
                "msg":objilist,
            }
            return render(request,'login/Login.html',context)
    return render(request,'login/Login.html')