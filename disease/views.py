from django.shortcuts import render
from disease.models import Disease
# Create your views here.


def add_disease(request):
    if request.method=='POST':
        obj=Disease()
        obj.disease_name=request.POST.get('diname')
        obj.disease_symptom=request.POST.get('disymptom')
        obj.disease_image=request.POST.get('file')
        obj.save()
    return render(request,'disease/Add_Disease.html')

def admin_manage_disease(request):
    obj=Disease.objects.all()
    context={
        'x':obj
    }
    return render(request,'disease/Admin_Manage_Disease.html',context)

def doctor_manage_disease(request):
    obj = Disease.objects.all()
    context = {
        'x': obj
    }
    return render(request,'disease/Doctor_View_and_Update_Disease.html',context)