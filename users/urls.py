from django.urls import path, include
from . import views

urlpatterns = [
  # path('', views.all_user, name="users"),
  path('', views.nav_login_user, name="nav_login"),
  path('logout/', views.logout_user, name="logout"),
]