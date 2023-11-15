from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def peper(request):
    return render(request, 'peper.html')

def periperi(request):
    return HttpResponse('<cenetr> I didnot eat alfarm for past 4 months now </center>')