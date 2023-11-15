from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def chicken(request):
    return render(request,'chicken.html')

def mutton(request):
    return HttpResponse('<marquee><h1>TASTY</h1></marquee>')