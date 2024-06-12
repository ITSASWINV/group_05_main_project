from django.shortcuts import render
from student.models import Student
from chat.models import Chat
import datetime
from django.db.models import Q
from alumini.models import Alumini
from chat.models import CareerPath
# Create your views here.
from login.models import Login
from Career.models import Prediction
from alumini.models import Alumini

def con(request):
    # ob= Alumini.objects.all()
    uid=request.session["u_id"]
    p=Prediction.objects.filter(student_id=uid)
    if p:
        pob=Prediction.objects.get(student_id=uid)
        ob=CareerPath.objects.filter(career=pob.career)
        context = {
            'u': ob
        }
        return render(request, 'chat/viewcon.html', context)
    else:
        message="Predict First"
        context={
            'msg':message
        }
        return render(request, 'temp/student.html',context)


def cochat(request,idd):
    ss=request.session["u_id"]
    obbj = Student.objects.get(student_id=ss)
    obj=CareerPath.objects.get(career_id=idd)
    ob = Chat.objects.filter(Q(student_id=ss))
    context = {
        'kk': ob,
        'uu': obj,
    }
    if request.method == 'POST':
        obk = Chat()
        obk.message = request.POST.get('mssg')
        obk.career_id=idd
        obk.student_id=ss
        obk.rectype="alumini"
        obk.sendertype = "student"
        obk.student=obbj.name
        obk.save()
    return render(request, 'chat/chatuser1.html',context)



def std(request):
    uid=request.session["u_id"]
    aob=Alumini.objects.get(alumini_id=uid)
    # ob=Student.objects.all()
    ob=CareerPath.objects.filter(career_id=aob.career_id)
    context={
        'u':ob
    }
    return render(request,'chat/view user.html',context)


def stchat(request,idd):
    ss = request.session["u_id"]
    obbj =Alumini.objects.get(alumini_id=ss)
    obj =CareerPath.objects.get(career_id=idd)
    # ob=Chat.objects.filter(Q(career_id=idd) & Q(alumini_id=ss))
    ob=Chat.objects.filter(Q(career_id=idd))
    context={
        'kk':ob,
        'uu':obj,
    }

    if request.method=='POST':
        obk=Chat()
        obk.message=request.POST.get('mssg')
        obk.career_id=idd
        obk.alumini_id=ss
        obk.rectype="student"
        obk.sendertype="alumini"
        obk.alumini=obbj.name
        obk.save()
    return render(request, 'chat/chatuser2.html',context)
