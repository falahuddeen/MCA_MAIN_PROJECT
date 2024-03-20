from django.shortcuts import render
from review.models import Review
from doctor_register.models import DoctorRegister
import datetime
# Create your views here.


def add_review(request):
    obj=DoctorRegister.objects.filter(status="Approved")
    data={
        'x':obj
    }
    if request.method=='POST':
        obj=Review()
        uid=request.session["u_id"]
        obj.user_id=uid
        obj.doctor_id=request.POST.get('dname')
        obj.review=request.POST.get('review')
        obj.date=datetime.datetime.today()
        obj.time=datetime.datetime.today()
        obj.save()
    return render(request,'review/Add_Review.html',data)

def admin_view_doctor_review(request):
    obj=Review.objects.all()
    data={
        'x':obj
    }
    return render(request,'review/Admin_View_Doctor_Review.html',data)

def doctor_view_review(request):
    uid=request.session["u_id"]
    obj = Review.objects.filter(doctor_id=uid)
    data = {
        'x': obj
    }
    return render(request,'review/Doctor_View_Review.html',data)

