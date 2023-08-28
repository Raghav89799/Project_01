from rest_framework import serializers
from .models import Company,Employee

class CompanySerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta :
        model = Company
        fields = "__all__"
        
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    
    class Meta :
        model = Employee
        fields = "__all__"
        
        