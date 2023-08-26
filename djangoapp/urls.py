from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from djangoapp.views import CompanyViewSet,EmployeeViewSet

router = routers.DefaultRouter()
router.register(r"Company",CompanyViewSet)
router.register(r"employee",EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls)),
    path('company',CompanyViewSet.as_view({'get': 'list'})),
]
 