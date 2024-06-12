from django.conf.urls import url
from temp import views

urlpatterns=[
    url('home/', views.home),
    url('admin/', views.admin),
    url('alumini/', views.alumini),
    url('company/', views.company),
    url('student/', views.student)
]