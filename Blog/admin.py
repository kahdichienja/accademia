from django.contrib import admin
from .models import Post
# Register your models here.

class PostModelAdmin(admin.ModelAdmin):
    list_display = ["title","author","created_at","photo"]
    list_display_links = ["author"]
    list_filter = ["author", "title"]
    search_fields = ["title","author"]
    class Meta:
        model = Post

admin.site.register(Post, PostModelAdmin)