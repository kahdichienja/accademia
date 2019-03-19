from __future__ import unicode_literals

from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models

# Create your models here.
class CommentManager(models.Manager):
    def all(self):
        qs = super(CommentManager, self).filter(parent = None)
        return qs
    def filter_by_instance(self, instance):
        content_type = ContentType.objects.get_for_model(instance.__class__)
        obj_id = instance.id
        qs = super(CommentManager, self).filter(content_type = content_type, object_id = obj_id).filter(parent = None)
        return qs
class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default = 1, on_delete=models.CASCADE)
    # post = models.ForeignKey(Post, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, null = True)
    object_id = models.PositiveIntegerField(null=True)
    content_object = GenericForeignKey('content_type', 'object_id')

    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)

    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = CommentManager()

    class Meta:
        ordering = ['-timestamp']

    def __unicode__(self):
        return str(self.user.username)
    def __str__(self):
        return str(self.user.username)  
    def children(self):#comments replies
        return Comment.objects.filter(parent=self) 
    @property    
    def is_parent(self):
        if self.parent is not None:
            return False 
        return True    
