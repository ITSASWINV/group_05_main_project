from django.conf.urls import url
from Career import views

urlpatterns=[
    url('Carrer/',views.career),
    url('vcar/',views.vcareer),
    # url('result/', views.result),
]