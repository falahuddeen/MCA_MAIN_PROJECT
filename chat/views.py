from django.shortcuts import render
from user_register.models import UserRegister
from chat.models import Chat
import datetime
from django.db.models import Q
from doctor_register.models import DoctorRegister
# Create your views here.
from login.models import Login


def con(request):
    ob= DoctorRegister.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/viewcon.html',context)

def cochat(request,idd):
    ss=request.session["u_id"]
    obj = DoctorRegister.objects.get(doctor_id=idd)
    ob = Chat.objects.filter(Q(user_id=ss) & Q(doctor_id=idd))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.doctor_id=idd
        obk.user_id=ss
        obk.rectype="doctor"
        obk.sendertype = "user"
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    ob=UserRegister.objects.all()
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obj =UserRegister.objects.get(user_id=idd)
    ob=Chat.objects.filter(Q(user_id=idd) & Q(doctor_id=ss))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.user_id=idd
        obk.doctor_id=ss
        obk.rectype="user"
        obk.sendertype="doctor"
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
