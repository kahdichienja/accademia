from django.db import models
from accounts.models import User
from django import forms
from datetime import datetime
# Create your models here.

class AssinmentType(models.Model):
    type_of_assignment= models.CharField(max_length = 254, blank=True, null=True)
    assignment_title = models.TextField(max_length = 254, blank=True, null=True)
    unit_name = models.CharField(max_length = 254, blank=True, null=True)
    unit_code = models.CharField(max_length = 254, blank=True, null=True)
    date = models.DateTimeField(default = datetime.now, blank = True)

class AssignmentSubmissionForm(models.Model):
    # not included on form bcoz is_authenticated
    full_name = models.CharField(max_length = 254, blank=True, null=True)
    admission_number = models.CharField(max_length = 254, blank=True, null=True)
    university = models.CharField(max_length = 254, blank=True, null=True)
    username = models.CharField(max_length = 254, blank=True, null=True)
    phone_number = models.CharField(max_length = 254, blank=True, null=True)
    type_of_assignment= models.CharField(max_length = 254, blank=True, null=True)
    unit_name = models.CharField(max_length = 254, blank=True, null=True)
    #End not included on form bcoz is_authenticated
    file_name = models.FileField(upload_to = 'documents/studentsassignments/', null = True, blank = True)
    date = models.DateTimeField(default = datetime.now, blank = True)
    AssinmentType = models.ManyToManyField(AssinmentType)
    accounts = models.ManyToManyField(User)

    def __str__(self):
        return self.admission_number

    def delete(self, *args, **kwargs):
        self.file_name.delete()
        super().delete(*args, **kwargs)     