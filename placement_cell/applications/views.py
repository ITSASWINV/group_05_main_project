from django.http import HttpResponseBadRequest
from django.shortcuts import render
from applications.models import Applications
import datetime
from jobs.models import Jobs
from student.models import Student
# Create your views here.

def c_app(request):
    ss= request.session["u_id"]
    obj = Applications.objects.filter(job__company_id=ss)
    context = {
        'b': obj
    }
    return render(request,'applications/company_manageapp.html', context)

def reject(request, idd):
    obj = Applications.objects.get(application_id=idd)
    obj.status = 'rejected'
    obj.save()
    return c_app(request)

def accept(request, idd):
    obj = Applications.objects.get(application_id=idd)
    obj.status = 'accepted'
    obj.save()
    return c_app(request)

def s_app(request):
    ss= request.session["u_id"]
    obj = Applications.objects.filter(student_id=ss)
    context = {
        'b': obj
    }
    return render(request,'applications/student_applicationstatus.html', context)

# def post_app(request, idd):
#     ss= request.session["u_id"]
#     ob = Jobs.objects.get(job_id=idd)
#     context = {
#         'a':ob
#     }
#     if request.method=='POST':
#         obj=Applications()
#         obj.job_id=idd
#         obj.student_id = ss
#         obj.date=datetime.datetime.today()
#         obj.time=datetime.datetime.now()
#         obj.save()
#
#
#     return render(request,'applications/post_application.html',context)



def post_app(request, idd):
    ss = request.session["u_id"]
    ob = Jobs.objects.get(job_id=idd)
    student = Student.objects.get(student_id=ss)
    context = {
        'a': ob
    }

    if request.method == 'POST':
        # Check if student skills match job skills
        if set(student.skills.split(',')) & set(ob.skills.split(',')):
            # If skills match, create and save application object
            obj = Applications()
            obj.job_id = idd
            obj.student_id = ss
            obj.date = datetime.datetime.today()
            obj.time = datetime.datetime.now()
            obj.save()
            return render(request, 'applications/post_application.html', context)
        else:
            # If skills don't match, return an error response
            return HttpResponseBadRequest("Your skills don't match the job requirements.")

    return render(request, 'applications/post_application.html', context)
