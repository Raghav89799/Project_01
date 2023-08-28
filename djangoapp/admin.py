from django.contrib import admin
from .models import *

# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
  list_display = ("name", "location", "phone","types","activate")

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name","company_name","position","phone_number")
    
    
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)

