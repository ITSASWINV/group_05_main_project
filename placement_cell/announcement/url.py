from django.conf.urls import url
from announcement import views

urlpatterns=[
    url('c_ann/', views.c_ann),
    url('s_ann/',views.s_ann),
    url('view_ad/', views.admin)
]