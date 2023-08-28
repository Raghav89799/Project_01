from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length = 50)
    location = models.CharField(max_length = 50)
    about = models.TextField(max_length = 200)
    phone = models.IntegerField()
    types = models.CharField(max_length = 50,choices = (("IT","IT"),("non IT","non IT"),("Mobile Phone","Mobile Phone")))
    activate = models.BooleanField(default = True)
    
    def __str__(self):
        return self.name
    
    
class Employee(models.Model):
    company_name = models.ForeignKey(Company,on_delete=models.CASCADE)
    name = models.CharField(max_length = 50)
    email = models.CharField(max_length = 70)
    phone_number = models.IntegerField()
    date_time = models.DateTimeField()
    position = models.CharField(blank=True,max_length = 50,choices = (("Manager","Manager"),("Software Developer","Software Developer"),("Labour","Labour")))
    
    def __str__(self):
        return self.name
    