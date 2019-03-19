from django.db import models
from datetime import datetime
from django.contrib.contenttypes.models import ContentType
from comments.models import Comment
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
        
    @property
    def comments(self):
        instance = self
        qs = Comment.objects.filter_by_instance(instance)
        return qs    

    @property
    def get_content_type(self):
        instance = self
        content_type = ContentType.objects.get_for_model(instance.__class__)
        return content_type