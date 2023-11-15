from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def fish(request):
    return render(request, 'fish.html')

def rice(request):
    return HttpResponse(request,'<h1>mandi rice is soooo good</h1>')