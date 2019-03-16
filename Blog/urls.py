from django.urls import path

from django.conf.urls.static import static
from django.conf import settings

from .import views


urlpatterns = [
    path('', views.blog_home, name = 'blog_home'),
    path('addpost/', views.add_post, name = 'add_post'),
    path('allposts/', views.all_posts, name = 'all_posts'),
    path('postitem/<id>', views.post_item, name = 'post_item'),
    path('postitemdelete/<id>/', views.delete_post, name='delete_post'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
