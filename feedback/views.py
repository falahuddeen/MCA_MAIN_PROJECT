from django.shortcuts import render
from feedback.models import Feedback
import datetime
# Create your views here.



def add_feedback(request):
    if request.method=='POST':
        obj=Feedback()
        obj.user_id=1
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