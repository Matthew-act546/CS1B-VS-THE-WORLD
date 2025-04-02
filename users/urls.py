from django.urls import path, include
from . import views

urlpatterns = [
  path('', views.all_user, name="users"),
  path('', include('django.contrib.auth.urls')),
]