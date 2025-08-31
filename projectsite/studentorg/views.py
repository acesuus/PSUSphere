from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("Django install worked successfully!")


# Create your views here.
