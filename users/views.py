from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def all_user(request):
  first_name = ["Matthew", "David", "Fernandez", "Chariss", "Salvador"]
  context = {"first_name": first_name, "nest": {"nested": 123}}
  return render(request, "user.html", context)
