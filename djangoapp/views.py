from django.shortcuts import render
from rest_framework import viewsets
from .models import Company,Employee
from .serializers import CompanySerializers,EmployeeSerializers
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.views import APIView
# Create your views here.

class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializers
    
    # companies/company{id}/employee
    @action(detail = True,methods = ['get'])
    def employee(self,request,pk=None):
        try:
            company = Company.object.get(pk=pk)
            employ = Employee.objects.filter(company=company)
            employ_serializer = EmployeeSerializers(employ,many=True,context = {'request':request})
            return Response(employ_serializer.data)
        except:
            return Response({
                "Message":"Company is not exist Error occured"
                })


class CompanyView(APIView):
    
    def get(self,request):
        instance = Company.objects.all()
        serializers = CompanySerializers(instance,many=True,context = {'request':request})
        return Response(serializers.data)
    
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
    
    @action(detail = True,methods = ['get'])
    def employee(self,request,pk=None):
        employ = Employee.objects.get(pk=pk)
        employ_serializer = EmployeeSerializers(employ,many=True,context = {'request':request})
        return Response(employ_serializer.data)
    

class EmployeeView(APIView):
    
    def get(self,request):
        instance = Employee.objects.all()
        serializers = EmployeeSerializers(instance,many=True,context = {'request':request})
        return Response(serializers.data)
    