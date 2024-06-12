from django.conf.urls import url
from jobs import views

urlpatterns=[
    url('add_job/', views.add_job),
    url('view_job/',views.view_job)

]