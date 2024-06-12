from django.shortcuts import render
from test_round.models import TestRound

# Create your views here.

def ctest_reg(request):
    if request.method=='POST':
        obj=TestRound()
        obj.test_link=request.POST.get('testLink')
        obj.save( )
    return render(request, 'test_round/company_conducttest.html')

def stest_join(request):
    ob = TestRound.objects.all()
    context = {
        'a': ob
    }

    return render(request, 'test_round/student_Mocktest.html', context)
