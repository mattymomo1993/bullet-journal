from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'home.html')

def animation(request):
    return render(request, 'animation.html')