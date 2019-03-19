from django.db import models
from django import forms
from datetime import datetime
# Create your models here.


class University(models.Model):
    name = models.CharField(max_length=30)
    timestamp = models.DateTimeField(default = datetime.now, blank = True)
    def __str__(self):
        fullname = self. name
        return fullname

class NotesUpload(models.Model):
    university = models.ForeignKey('University', on_delete=models.CASCADE)
    unit_name = models.CharField(max_length=30)
    unit_code = models.CharField(max_length=30)
    Comment = models.TextField()
    notes_file = models.FileField(upload_to = 'Notes/universitynotes/', null = True, blank = True)
    timestamp = models.DateTimeField(default = datetime.now, blank = True)

    def __str__(self):
        return self.unit_name
