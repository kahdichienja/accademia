from rest_framework.serializers import ModelSerializer

from Blog.models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id',
            'title',
            'author', 
            'description', 
            'photo',
            'created_at'
        ]