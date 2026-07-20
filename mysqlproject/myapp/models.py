from django.db import models

# Create your models here.
class Employee(models.Model):
    name=models.CharField()
    email=models.EmailField()
    job=models.CharField()