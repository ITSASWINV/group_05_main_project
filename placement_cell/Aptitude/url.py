from django.conf.urls import url
from Aptitude import views

urlpatterns=[
    url('Aptitude/',views.place),
    url('result/',views.result),
    url('view_res/',views.view_prediction)
]