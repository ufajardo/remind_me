from django.db import models

# Create your models here.

class Employee(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.CharField(max_length=50, default="None")



class License(models.Model):
    state = models.CharField(max_length=30)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    expiration = models.DateField()
