
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from .import views
urlpatterns = [
    path('home/', views.assignments_home, name = 'assignments_home'),
    path('submitions/', views.submit_assignment_view, name = 'submit_assignment_view'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)