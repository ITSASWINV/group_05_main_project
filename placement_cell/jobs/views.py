from django.shortcuts import render
from jobs.models import Jobs
import datetime
# Create your views here.
def add_job(request):
    ss= request.session["u_id"]
    if request.method=='POST':
        obj=Jobs()
        obj.name=request.POST.get('name')
        obj.role=request.POST.get('role')
        obj.skills=request.POST.get('skills')
        obj.compensation=request.POST.get('compensation')
        obj.location=request.POST.get('location')
        obj.description=request.POST.get('description')
        obj.post_time = datetime.datetime.now()
        obj.company_id = ss
        obj.save()
    return render(request, 'jobs/add_job.html')


def view_job(request):
    ob = Jobs.objects.all()
    context = {
        'a': ob
    }

    return render(request,'jobs/st_job.html', context)