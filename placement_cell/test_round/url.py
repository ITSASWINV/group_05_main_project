from django.conf.urls import url
from test_round import views

urlpatterns=[
    url('ctest_reg/', views.ctest_reg),
    url('stest_join/',views.stest_join)
]