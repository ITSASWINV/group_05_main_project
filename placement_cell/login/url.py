from django.conf.urls import url
from login import views

urlpatterns=[
    url('admin_login/', views.login)

]