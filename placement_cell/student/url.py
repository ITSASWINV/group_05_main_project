from django.conf.urls import url
from student import views

urlpatterns=[
    url('std_reg/', views.s_reg),
    url('std_mng/', views.mng_s),
    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),
    url('al_view/', views.alumini),
    url('resume/',views.pdf_resume),

    url('project/',views.add_project),
    url('internship/',views.add_internship),
]