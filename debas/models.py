from django.db import models
from django.urls import reverse

# Create your models here.
class Studentdb(models.Model):
    studentId = models.AutoField
    rollno = models.CharField(max_length=7, default='')
    name = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.rollno
    