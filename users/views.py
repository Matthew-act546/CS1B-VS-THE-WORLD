from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.
def nav_login_user(request):
  if request.method == "POST":
    student_num = request.POST["username"]
    password = request.POST["password"]
    user = authenticate(request, username=student_num, password=password)
    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'error infasd')
      return redirect('home')
  else:
    return render(request, "index.html")
  
def logout_user(request):
  logout(request)
  messages.success(request, 'you successfully logout')
  return redirect('home')
