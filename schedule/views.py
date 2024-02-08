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
