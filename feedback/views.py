from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.



def add_feedback(request):
    if request.method=='POST':
        obj=Feedback()
        uid=request.session["u_id"]
        obj.user_id=uid
        obj.feedback=request.POST.get('feedback')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'feedback/Add_Feedback.html')

def view_feedback(request):
    obj=Feedback.objects.all()
    data={
        'x':obj
    }
    return render(request,'feedback/Admin_View_Feedback.html',data)