from django.db import models

# Create your models here.

#Creating Company Model
class Company(models.Model):
    company_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=50)
    type = models.TextField(choices=(('IT','IT'),
                                     ("Non IT","Non IT"),
                                     ('Mobile Phone',"Mobile Phone"),
                                     ))
    date_time = models.DateTimeField(auto_now=True)
    about = models.TextField(blank=False,max_length=500)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

#Creating Employee Model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=200)
    email = models.EmailField(max_length=70)
    phone_number = models.IntegerField(max_length=10)
    about = models.TextField(max_length=500)
    position = models.TextField(choices=(("Manager","Manager"),
                                         ("Software Developer","Software Seveloper"),
                                         ("Project Leader","Project Leader")
                                         ))
    company = models.ForeignKey(Company,on_delete=models.CASCADE)
