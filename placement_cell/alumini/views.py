from django.shortcuts import render
from alumini.models import Alumini
# Create your views here.
from login.models import Login
from chat.models import CareerPath

def reg(request):
    ob=CareerPath.objects.all()
    context={
        'x':ob
    }
    if request.method=='POST':
        obj=Alumini()
        obj.name=request.POST.get('name')
        obj.mail=request.POST.get('mail')
        obj.phone=request.POST.get('phone')
        obj.career_path=request.POST.get('careerpath')
        obj.experience=request.POST.get('experience')
        obj.year=request.POST.get('year')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.save()
    return  render(request,'alumini/al_register.html',context)

def mng_al(request):
    obj = Alumini.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'alumini/admin_manage_alumini.html', context)

def accept(request, idd):
    obj = Alumini.objects.get(alumini_id=idd)
    obj.status = 'accepted'
    obj.save()

    ob = Login()
    ob.username = obj.mail
    ob.password = obj.password
    ob.u_id = obj.alumini_id
    ob.type = 'alumini'
    ob.save()
    return mng_al(request)


def reject(request, idd):
    obj = Alumini.objects.get(alumini_id=idd)
    obj.status = 'rejected'
    obj.save()
    return mng_al(request)


def st_view(request):
    obj = Alumini.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'alumini/view_student.html', context)