from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
# Create your views here.

def index(request):
    return render(request,'land/create.html')

def transfer(request):
    return render(request,'land/transfer.html')

def register(request):
    return render(request,'land/register.html')
