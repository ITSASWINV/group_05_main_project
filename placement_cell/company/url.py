from django.conf.urls import url
from company import views

urlpatterns=[
    url('c_reg/', views.c_reg),
    url('mng_c/', views.mng_c),
    url('accept/(?P<idd>\w+)', views.accept),
    url('reject/(?P<idd>\w+)', views.reject),
    url('view_sttt/', views.st_view)
]