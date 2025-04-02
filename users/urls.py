from django.urls import path, include
from . import views

urlpatterns = [
  # path('', views.all_user, name="users"),
  path('login/', views.login_user, name="login"),
]