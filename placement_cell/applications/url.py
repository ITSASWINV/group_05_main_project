from django.conf.urls import url
from applications import views

urlpatterns=[
    url('c_app/', views.c_app),
    url('s_app/',views.s_app),
    url('post_app/(?P<idd>\w+)',views.post_app),
    url('accept/(?P<idd>\w+)',views.accept),
    url('reject/(?P<idd>\w+)',views.reject)
]