from django.shortcuts import render
from user_register.models import UserRegister
# Create your views here.



def admin_view_user(request):
    obj=UserRegister.objects.all()
    data={
        'x':obj
    }
    return render(request,'user_register/Admin_View_Users.html',data)

def user_registration(request):
    if request.method=='POST':
        obj=UserRegister()
        obj.name=request.POST.get('uname')
        obj.mobile=request.POST.get('umobile')
        obj.age=request.POST.get('uage')
        obj.gender=request.POST.get('Gender')
        obj.password=request.POST.get('pass')
        obj.save()
    return render(request,'user_register/User_Registration.html')

def user_view_profile(request):
    obj = UserRegister.objects.all()
    data = {
        'x': obj
    }
    return render(request,'user_register/User_View_Profile.html',data)