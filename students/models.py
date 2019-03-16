from django.db import models
from django import forms
from datetime import datetime
# Create your models here.

class StudentRegisterForm(models.Model):
    first_name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    admission_number = models.CharField(max_length=30)
    phone_number = models.IntegerField()
    email = models.EmailField(max_length=254, unique=True, verbose_name='email address')
    university = models.CharField(max_length=30)
    password = models.CharField(max_length = 100) 
    password2 = models.CharField(max_length = 100)
    timestamp = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        fullname = self.first_name +" "+ self.surname +" "+ self.last_name
        return fullname