from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.list import ListView
from studentorg.models import Organization

class HomePageView(ListView):
    model = Organization
    context_object_name = 'home'
    template_name = "home.html"

def home(request):
    return HttpResponse("Django install worked successfully!")


# Create your views here.
