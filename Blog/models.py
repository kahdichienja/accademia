from django.db import models
from datetime import datetime
# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length = 100)
    author = models.CharField(max_length = 100)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(default = datetime.now, blank = True)
    photo = models.ImageField(upload_to = 'photos/blogphotos/', null = True, blank = True)
    def __str__(self):
        return self.title

    def delete(self, *args, **kwargs):
        self.photo.delete()
        super().delete(*args, **kwargs)    