from django.conf.urls import url
from alumini import views

urlpatterns=[
    url('alumini_add/', views.reg),
    url('manage_almni/', views.mng_al),
    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),
    url('st_view/', views.st_view)

]