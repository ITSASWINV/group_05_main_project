from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'temp/home.html')


def admin(request):
    return render(request, 'temp/admin.html')


def alumini(request):
    return render(request, 'temp/alumini.html')


def company(request):
    return render(request, 'temp/company.html')


def student(request):
    return render(request, 'temp/student.html')