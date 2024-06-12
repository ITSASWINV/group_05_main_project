from django.shortcuts import render
from announcement.models import Announcement
from jobs.models import Jobs
import datetime
# Create your views here.

def c_ann(request):
    ss= request.session["u_id"]
    ob = Jobs.objects.all()
    context = {
        'd':ob
    }
    if request.method =='POST':
        obj = Announcement()
        obj.job_id = request.POST.get('jbname')
        obj.company_id = ss
        obj.vacancy = request.POST.get('vancy')
        obj.date = datetime.datetime.today()
        obj.save()

    return render(request, 'announcement/company_announcemet.html', context)

def s_ann(request):
    obj = Announcement.objects.all()
    context = {
        'w': obj
    }
    return render(request, 'announcement/student_announcement.html', context)

def admin(request):
    obj = Announcement.objects.all()
    context = {
        'w': obj
    }
    return render(request, 'announcement/admin_view.html', context)

