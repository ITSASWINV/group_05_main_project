from django.shortcuts import render
from placement_cell import settings
from pandas import read_excel
from sklearn.tree import DecisionTreeClassifier
from Career.models import Prediction
from student.models import Student
# Create your views here


def career(request):
    uid=request.session["u_id"]
    sob=Student.objects.get(student_id=uid)
    context={
        'cgpa':sob.cgpa
    }
    if request.method=='POST':
        print("start")
        a1=request.POST.get('q1')
        print(a1)
        a2=request.POST.get('q2')
        print(a2)
        a3=request.POST.get('q3')
        print(a3)
        a4=request.POST.get('q4')
        print(a4)
        a5=request.POST.get('q5')
        print(a5)
        a6=request.POST.get('q6')
        print(a6)
        a7 = request.POST.get('q7')
        print(a7)
        a8=request.POST.get('q8')
        print(a8)
        a9 = request.POST.get('q9')
        print(a9)
        a10 = request.POST.get('q10')
        print(a10)
        a11 = request.POST.get('q11')
        print(a11)
        a12 = request.POST.get('q12')
        print(a12)
        a13 = request.POST.get('q13')
        print(a13)
        a14 = request.POST.get('q14')
        print(a14)
        a15 = request.POST.get('q15')
        print(a15)
        a16 = request.POST.get('q16')
        print(a16)
        a17 = request.POST.get('q17')
        print(a17)
        a18 = request.POST.get('q18')
        print(a18)
        a19 = request.POST.get('q19')
        print(a19)
        a20 = request.POST.get('q20')
        print(a20)
        a21 = request.POST.get('q21')
        print(a21)
        a22 = request.POST.get('q22')
        print(a22)
        a23 = request.POST.get('q23')
        print(a23)
        a24 = request.POST.get('q24')
        print(a24)
        a25 = request.POST.get('q25')
        print(a25)
        a26 = request.POST.get('q26')
        print(a26)
        a27 = request.POST.get('q27')
        print(a27)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "cs.xls"
        data = read_excel(imgpath, "cs")
        print(data.head())
        # X = data.iloc[:, 0:27].values
        # y = data.iloc[:, 27].values
        X = data.iloc[:, :27].values
        y = data.iloc[:, 27].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        test = [
            float(a1), float(a2), float(a3), float(a4), float(a5), float(a6), float(a7), float(a8), float(a9), float(a10), float(a11),
            float(a12), float(a13), float(a14), float(a15), float(a16), float(a17), float(a18), float(a19), float(a20), float(a21),
            float(a22), float(a23), float(a24), float(a25), float(a26), float(a27)
        ]

        print("test")
        print(test)

        # test = [int(a1), int(a2), int(a3), int(a4), int(a5), int(a6),int(a7), int(a8),int(a8)]

        y_pred = dtc.predict([test])
        #
        print(y_pred)
        k=str(y_pred[0])
        ss=request.session["u_id"]

        if k:
            if Prediction.objects.filter(student_id=ss).exists():
                obbb=Prediction.objects.get(student_id=ss)
            else:
                obbb=Prediction()
            obbb.student_id=ss
            obbb.career=k
            obbb.save()

        context = {
            'bb': k
        }
        return render(request, 'Career/result.html', context)
    return render(request,'Career/tech.html',context)




def vcareer(request):
    obj =Prediction.objects.all()
    context = {
        'x': obj
    }
    return render(request,'Career/vcareer.html',context)

