from django.shortcuts import render
from django.http import HttpResponse
from .models import User

# Create your views here.
def all_user(request):
  first_name = ["Matthew", "David", "Fernandez", "Chariss", "Salvador"]

  users_list = User.objects.all()
  context = {'users': users_list}
  return render(request, "user.html", context)
