from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def login_user(request):
  if request.method == "POST":
    student_num = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=student_num, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'error infasd')
      return redirect('login')
  else:
    return render(request, "authentication/login.html")
