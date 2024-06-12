from django.http import HttpResponseRedirect
from django.shortcuts import render
from login.models import Login
from student.models import Student
# Create your views here.


def login(request):
    if request.method == "POST":
        eml = request.POST.get("un")
        passw = request.POST.get("ps")
        obj = Login.objects.filter(username=eml,password=passw)
        tp = ""
        for ob in obj:
            tp = ob.type
            uid = ob.u_id
            if tp == "admin":
                request.session["u_id"]=uid
                return HttpResponseRedirect('/temp/admin/')
            elif tp == "student":
                uob=Student.objects.get(student_id=uid)
                if uob.status=='accepted':
                    request.session["u_id"]=uid
                    return HttpResponseRedirect('/temp/student/')
                else:
                    message="Your registration is pending"
                    context = {
                        'msg': message,
                    }
                    return render(request, 'login/admin_login.html', context)
            elif tp == "alumini":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/alumini/')
            elif tp == "company":
                request.session["u_id"] = uid
                return HttpResponseRedirect('/temp/company/')
        objlist ="email or password incorrect.....please try again.....!"
        context = {
            'msg':objlist,
        }
        return render(request,'login/admin_login.html',context)
    return render(request,'login/admin_login.html')