from django.shortcuts import render

# Create your views here.

def home(request):
  context = {'number': 43}
  return render(request, 'index.html', context)