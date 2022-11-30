from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    lap=Laptop.objects.all()    # Select * from Laptop
    lap_dict = {
        'lap': lap
    }
    return render(request,'index.html',lap_dict)

def index2(request):
    return HttpResponse('hola. index2')

def index3(request):
    return HttpResponse('hola. index3')