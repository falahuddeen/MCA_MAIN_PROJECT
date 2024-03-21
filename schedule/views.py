from django.shortcuts import render
from schedule.models import Schedule
import datetime
# Create your views here.



def schedule_management(request):
    did=request.session["u_id"]
    obj=Schedule.objects.filter(doctor_id=did)
    data={
        'x':obj
    }
    return render(request,'schedule/Doctor_Schedule_Managment.html',data)
def doctor_schedule_update(request,idd):
    obj=Schedule.objects.get(schedule_id=idd)
    data={
        'x':obj
    }
    if request.method=="POST":
        obj = Schedule.objects.get(schedule_id=idd)
        uid = request.session["u_id"]
        obj.doctor_id = uid
        obj.schedule = request.POST.get('schedule')
        obj.date = datetime.datetime.today()
        obj.time = datetime.datetime.today()
        obj.save()
        return schedule_management(request)
    return render(request,'schedule/Doctor_Schedule_Update.html',data)

def doctor_schedule_delete(request,idd):
    obj=Schedule.objects.get(schedule_id=idd)
    obj.delete()
    return schedule_management(request)

def schedule(request):
    uid=request.session["u_id"]
    ob = Schedule.objects.filter(doctor_id=uid)
    if ob!='':
        message = "You Already Added a Schedule, So Update it.."
        context = {
            'msg': message,
        }
        return render(request, 'temp/doctor.html', context)
    if request.method=='POST':
        obj=Schedule()
        uid=request.session["u_id"]
        obj.doctor_id=uid
        obj.schedule=request.POST.get('schedule')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'schedule/Schedule.html')

def view_schedule(request):
    obj = Schedule.objects.all()
    data = {
        'x': obj
    }
    return render(request,'schedule/User_View_Doctors_Schedule.html',data)
