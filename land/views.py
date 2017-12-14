from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from .forms import CreateForm, TransferForm, RegisterForm
# Create your views here.

def create(request):
    return render(request,'land/create.html')

def transfer(request):
    return render(request,'land/transfer.html')

def register(request):
    return render(request,'land/register.html')

class CreateView(FormView):
    form_class = CreateForm
    template_name = 'land/create.html'
    success_url = '/success'
    def form_valid(self,form):
        # Post on IPDB
        return super().form_valid(self,form)

class TransferView(FormView):
    form_class = TransferForm
    template_name = 'land/transfer.html'

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'land/register.html'
