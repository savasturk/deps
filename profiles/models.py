from django.db import models
from django.contrib.auth.models import User as DjangoUser
#This project uses Django Authentication System
#For more information visit: https://docs.djangoproject.com/en/1.11/topics/auth/default/

EducationTypes = ((1, "Örgün öğretim"), (2, "İkinci Öğretim"), (3, "Yüksek Lisans"), (4,("Doktora")))

class User(models.Model):
    user = models.OneToOneField(DjangoUser, on_delete=models.CASCADE)
    birth_date = models.DateField()
    student_number = models.IntegerField()
    faculty = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    grade = models.IntegerField(default=1, choices=EducationTypes)
    verified = models.BooleanField(default=0)