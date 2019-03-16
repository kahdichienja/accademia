
from django.urls import path, include
# from .import views
from .views import RegisterView, LoginView
urlpatterns = [
    # path('', views.home_view, name = 'home_view'),
    path('register/', RegisterView.as_view(), name = 'register'),
    path('login/', LoginView.as_view(), name = 'login'),


]