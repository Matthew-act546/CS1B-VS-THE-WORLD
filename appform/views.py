from django.shortcuts import render

# Create your views here.

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def announcements(request):
  return render(request, 'announcements.html')

def register(request):
  return render(request, 'sign-up.html')
