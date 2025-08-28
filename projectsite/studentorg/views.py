from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hi Maam")


# Create your views here.
