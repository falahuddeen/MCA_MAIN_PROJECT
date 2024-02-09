from django.shortcuts import render
from schedule.models import Schedule
import datetime
# Create your views here.



def schedule_management(request):
    obj=Schedule.objects.all()
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
        obj.doctor_id = 1
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
    if request.method=='POST':
        obj=Schedule()
        obj.doctor_id=1
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
