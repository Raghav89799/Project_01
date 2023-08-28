from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from djangoapp.views import *

router = routers.DefaultRouter()
router.register("company",CompanyViewSet)
router.register("employee",EmployeeViewSet)

urlpatterns = [
    path('app/',include(router.urls)),
    path('company/',CompanyView.as_view()),
    path('employee/',EmployeeView.as_view()),
]