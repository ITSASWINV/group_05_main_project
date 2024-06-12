from django.shortcuts import render
from student.models import Student,Project,Internship
from login.models import Login
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa


# Create your views here.
def s_reg(request):
    if request.method=='POST':
        obj=Student()
        obj.name=request.POST.get('name')
        obj.department=request.POST.get('department')
        obj.semester=request.POST.get('semester')
        obj.cgpa=request.POST.get('cgpa')
        obj.certificates=request.POST.get('certifications')
        obj.mail=request.POST.get('mail')
        obj.phone=request.POST.get('phone')
        obj.password=request.POST.get('password')
        obj.status='pending'
        obj.skills=request.POST.get('skill')
        myfile=request.FILES['photo']
        fs=FileSystemStorage()
        filename=fs.save(myfile.name,myfile)
        obj.photo=myfile.name
        obj.year=request.POST.get('year')
        obj.place=request.POST.get('place')
        obj.summary=request.POST.get('summary')
        obj.ucity=request.POST.get('ucity')
        obj.save( )
        ob = Login()
        ob.username = obj.mail
        ob.password = obj.password
        ob.u_id = obj.student_id
        ob.type = 'student'
        ob.save()
        message="Successfully Registered.."
        context={
            'msg':message
        }
        return render(request, 'student/st_register.html',context)
    return render(request, 'student/st_register.html')


def add_project(request):
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Project()
        obj.title=request.POST.get('name')
        obj.description=request.POST.get('skill')
        obj.student_id=uid
        obj.save( )
    return render(request, 'student/add_project.html')


def add_internship(request):
    uid=request.session["u_id"]
    if request.method=='POST':
        obj=Internship()
        obj.course=request.POST.get('name')
        obj.duration=request.POST.get('department')
        obj.student_id=uid
        obj.company=request.POST.get('company')
        obj.description=request.POST.get('skill')
        obj.save( )
    return render(request, 'student/add_internship.html')


def mng_s(request):
    obj = Student.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'student/admin_manage_student.html',context)

def pdf_resume(request):
    ss=request.session["u_id"]
    ob=Student.objects.get(student_id=ss)
    obj=Project.objects.filter(student_id=ss)
    obj1=Internship.objects.filter(student_id=ss)

    context = {
        'x': ob,
        'p':obj,
        'ii':obj1,
        'request': request  # Add the request object to the context
    }
    return render(request,'student/resume.html',context)
    # template_path = 'student/resume.html'
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="student_resume.pdf"'

    template = get_template(template_path)
    html = template.render(context, request)

    # Create PDF
    pisa_status = pisa.CreatePDF(html, dest=response)

    # If error, return HTML error page
    if pisa_status.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def accept(request, idd):
    obj = Student.objects.get(student_id=idd)
    obj.status = 'accepted'
    obj.save()

    return mng_s(request)


def reject(request, idd):
    obj = Student.objects.get(student_id=idd)
    obj.status = 'rejected'
    obj.save()
    return mng_s(request)


def alumini(request):
    obj = Student.objects.all()
    context = {
        'a': obj
    }
    return  render(request, 'student/view_alumini.html',context)