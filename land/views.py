from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from .forms import CreateForm, TransferForm, RegisterForm
from django.contrib import messages 

# Create your views here.

def success(request):
    return render(request,'land/success.html')

class CreateView(FormView):
    form_class = CreateForm
    template_name = 'land/create.html'
    success_url = '/create'
    def form_valid(self,form):
        
        if form.is_valid():
            f = form.cleaned_data
            # Post on IPDB
            # Register with database
            messages.success(self.request, f)
        return super().form_valid(form)

class TransferView(FormView):
    form_class = TransferForm
    template_name = 'land/transfer.html'
    success_url = '/transfer'
    def form_valid(self,form):
        # Post on IPDB
        if form.is_valid():
            f = form.cleaned_data
        messages.success(self.request, f) 
        return super().form_valid(form)

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'land/register.html'
    success_url = '/success'
    def form_valid(self,form):
        
        if form.is_valid():
            f = form.cleaned_data
            # Register to DataBase
            messages.success(self.request, f)
        return super().form_valid(form)
