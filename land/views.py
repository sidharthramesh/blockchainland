from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,'land/create.html')

def transfer(request):
    return render(request,'land/transfer.html')
