from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    roll = models.IntegerField()
    school = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    