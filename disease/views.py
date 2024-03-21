from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from disease.models import Disease
# Create your views here.


def add_disease(request):
    if request.method=='POST':
        obj=Disease()
        obj.disease_name=request.POST.get('diname')
        obj.disease_symptom=request.POST.get('disymptom')

        myfile1 = request.FILES["file"]
        fs = FileSystemStorage()
        filname = fs.save(myfile1.name, myfile1)
        obj.disease_image=myfile1.name

        obj.save()
    return render(request,'disease/Add_Disease.html')

def admin_manage_disease(request):
    obj=Disease.objects.all()
    context={
        'x':obj
    }
    return render(request,'disease/Admin_Manage_Disease.html',context)

def admin_update(request,idd):
    obj = Disease.objects.get(disease_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Disease.objects.get(disease_id=idd)
        obj.disease_name=request.POST.get('diname')
        obj.disease_symptom=request.POST.get('disymptom')

        myfile1 = request.FILES["file"]
        fs = FileSystemStorage()
        filname = fs.save(myfile1.name, myfile1)
        obj.disease_image = myfile1.name
        obj.save()
        return admin_manage_disease(request)
    return render(request, 'disease/Admin_Update.html', context)

def admin_delete(request,idd):
    obj=Disease.objects.get(disease_id=idd)
    obj.delete()
    return admin_manage_disease(request)

def doctor_manage_disease(request):
    obj = Disease.objects.all()
    context = {
        'x': obj
    }
    return render(request,'disease/Doctor_View_and_Update_Disease.html',context)


def doctor_update(request,idd):
    obj = Disease.objects.get(disease_id=idd)
    context = {
        'x': obj
    }
    if request.method=='POST':
        obj=Disease.objects.get(disease_id=idd)
        obj.disease_name=request.POST.get('diname')
        obj.disease_symptom=request.POST.get('disymptom')

        myfile1 = request.FILES["file"]
        fs = FileSystemStorage()
        filname = fs.save(myfile1.name, myfile1)
        obj.disease_image = myfile1.name

        obj.save()
        return admin_manage_disease(request)
    return render(request, 'disease/Doctor_Update.html', context)

def doctor_delete(request,idd):
    obj=Disease.objects.get(disease_id=idd)
    obj.delete()
    return doctor_manage_disease(request)