from django.shortcuts import render
from placement_cell import settings
from pandas import read_excel
from sklearn.tree import DecisionTreeClassifier
from Aptitude.models import Placement
# Create your views here.
def aptitude(request):
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
        a8 = request.POST.get('q8')
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
        a28 = request.POST.get('q28')
        print(a28)
        a29 = request.POST.get('q29')
        print(a29)
        a30 = request.POST.get('q30')
        print(a30)
        a31 = request.POST.get('q31')
        print(a31)
        a32 = request.POST.get('q32')
        print(a32)
        a33 = request.POST.get('q33')
        print(a33)
        # a34 = request.POST.get('q34')
        # print(a34)
        # a35 = request.POST.get('q35')
        # print(a35)
        # a36 = request.POST.get('q36')
        # print(a36)
        # a37 = request.POST.get('q37')
        # print(a37)
        # a38 = request.POST.get('q38')
        # print(a38)
        # a39 = request.POST.get('q39')
        # print(a39)
        # a40 = request.POST.get('q40')
        # print(a40)
        # a41 = request.POST.get('q41')
        # print(a41)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "person.xlsx"
        data = read_excel(imgpath, "Sheet1")
        X = data.iloc[:, 0:33].values
        y = data.iloc[:, 33].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        # test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),
        #         int(a13),int(a14),int(a15),int(a16),int(a17),int(a18),int(a19),int(a20),int(a21),int(a22),int(a23),int(a24),
        #         int(a25),int(a26),int(a27),int(a28),int(a29),int(a30),int(a31),int(a32),int(a33),int(a34),int(a35),int(a36),
        #         int(a37),int(a38),int(a39),int(a40),int(a41)]

        test = [int(a1), int(a2), int(a3), int(a4), int(a5), int(a6), int(a7), int(a8), int(a9), int(a10), int(a11),
                int(a12),
                int(a13), int(a14), int(a15), int(a16), int(a17), int(a18), int(a19), int(a20), int(a21), int(a22),
                int(a23), int(a24),
                int(a25), int(a26), int(a27), int(a28), int(a29), int(a30), int(a31), int(a32), int(a33),
                ]
        y_pred = dtc.predict([test])
        #
        print(y_pred)
        k=str(y_pred[0])
        context={
            'aa':k
        }
        return render(request,'Aptitude/result.html',context)
    return render(request,'Aptitude/Apptitude.html')


def result(request):
    return render(request,'Aptitude/result.html')

from student.models import Student
def place(request):
    uid=request.session["u_id"]
    ob=Student.objects.get(student_id=uid)
    if Placement.objects.filter(student_id=uid).exists():
        message="Already predicted"
        context={
            'msg':message
        }
        return render(request,'temp/student.html',context)

    if request.method=='POST':
        print("start")
        a1=request.POST.get('q1')
        print(a1)
        # a2=ob.
        # print(a2)
        a3=request.POST.get('q3')
        print(a3)
        a4=request.POST.get('q4')
        print(a4)
        # a5=request.POST.get('q5')
        a5=ob.cgpa
        print(a5)
        # a6=request.POST.get('q6')
        # print(a6)
        a7 = request.POST.get('q7')
        print(a7)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "collegePlace11.xlsx"
        data = read_excel(imgpath, "collegePlace")
        X = data.iloc[:, 0:5].values
        y = data.iloc[:, 5].values
        dtc = DecisionTreeClassifier()
        dtc.fit(X, y)
        # test = [int(a1),int(a2),int(a3),int(a4),int(a5),int(a6),int(a7),int(a8),int(a9),int(a10),int(a11),int(a12),
        #         int(a13),int(a14),int(a15),int(a16),int(a17),int(a18),int(a19),int(a20),int(a21),int(a22),int(a23),int(a24),
        #         int(a25),int(a26),int(a27),int(a28),int(a29),int(a30),int(a31),int(a32),int(a33),int(a34),int(a35),int(a36),
        #         int(a37),int(a38),int(a39),int(a40),int(a41)]

        test = [int(a1), int(a3), int(a4), int(a5), int(a7)]


        y_pred = dtc.predict([test])
        #
        print(y_pred)
        k=str(y_pred[0])

        if k:
            # if Placement.objects.filter(student_id=uid).exists():
            #     obbb=Placement.objects.get(student_id=uid)
            # else:
            obbb=Placement()
            obbb.student_id=uid
            obbb.backlogs=a7
            obbb.cgpa=a5
            obbb.internship=a4
            obbb.stream=a3
            obbb.status=k
            obbb.save()

        context={
            'aa':k
        }
        return render(request,'Aptitude/result.html',context)
    return render(request,'Aptitude/place.html')


def view_prediction(request):
    ob=Placement.objects.all()
    context={
        'x':ob
    }
    return render(request,'Aptitude/view_prediction.html',context)


