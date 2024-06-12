from django.shortcuts import render
from company.models import Company
# Create your views here.
from login.models import Login


def c_reg(request):
    if request.method=='POST':
        obj=Company()
        obj.name=request.POST.get('name')
        obj.mail=request.POST.get('email')
        obj.phone=request.POST.get('phone')
        obj.about=request.POST.get('description')
        obj.password=request.POST.get('password')
        obj.status='pending'

        obj.save( )
    return render(request, 'company/signup.html')

def mng_c(request):
    obj = Company.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'company/admin_manage_comp.html', context)

def accept(request, idd):
    obj = Company.objects.get(company_id=idd)
    obj.status = 'accepted'
    obj.save()

    ob = Login()
    ob.username = obj.mail
    ob.password = obj.password
    ob.u_id = obj.company_id
    ob.type = 'company'
    ob.save()
    return mng_c(request)


def reject(request, idd):
    obj = Company.objects.get(company_id=idd)
    obj.status = 'rejected'
    obj.save()
    return mng_c(request)

def st_view(request):
    obj = Company.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'company/view_t.html', context)