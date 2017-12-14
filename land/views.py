from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, FormView
from .forms import CreateForm, TransferForm, RegisterForm
from django.contrib import messages 
from .bigchainland import generate_keypair, create_land, transfer_land, get_transactions, CryptoKeypair
from .models import Land, CryptoUser
from blockchainland.settings import gov_public_key
# Create your views here.

def generate(request):
    key = generate_keypair()
    return render (request,'land/generate.html',{'key':key})

class CreateView(FormView):
    form_class = CreateForm
    template_name = 'land/create.html'
    success_url = '/create/'
    def form_valid(self,form):
        
        if form.is_valid():
            f = form.cleaned_data
            # Post on IPDB
            gov = CryptoKeypair(f.get('government_private_key'), gov_public_key)
            try:
                land = create_land(gov, {
                    "name":f.get('name'),
                    "other_attributes":f.get('other_attributes')
                })
                asset_id = land['id']
                # Register with database
                land_obj = Land.objects.create(name=f.get('name'),asset_id=asset_id)
                messages.success(self.request, 'Successfully created land asset!')
            except Exception as e:
                messages.success(self.request, e, 'error')
            
            
        return super().form_valid(form)

class TransferView(FormView):
    form_class = TransferForm
    template_name = 'land/transfer.html'
    success_url = '/transfer/'
    def form_valid(self,form):
        # Post on IPDB
        if form.is_valid():
            f = form.cleaned_data
            asset = f.get('asset')
            current_priv = f.get('owner_private_key')
            current_pub = asset.get_public_key(asset.get_transactions()[-1])
            current_owner = CryptoKeypair(current_priv, current_pub)
            new_owner = f.get('receipient_public_key')
            price = f.get('price')
            try:
                transfer = transfer_land(asset.asset_id, current_owner, new_owner,{'price':price})
                messages.success(self.request, "Transfer successful!")
            except Exception as e:
                messages.success(self.request, e, "error")
        return super().form_valid(form)

class RegisterView(FormView):
    form_class = RegisterForm
    template_name = 'land/register.html'
    success_url = '/register/'
    def form_valid(self,form):
        
        if form.is_valid():
            f = form.cleaned_data
            # Register to DataBase
            try:
                CryptoUser.objects.create(name=f.get('name'),public_key=f.get('public_key'))
                messages.success(self.request, 'You have successfully registered')
            except Exception as e:
                messages.success(self.request, e, 'error')
        return super().form_valid(form)
class LandListView(ListView):
    model = Land
    template_name = 'land/land_list.html'
    context_object_name = 'lands'
    query_set = Land.objects.all()

class LandDetailView(DetailView):
    model = Land
    template_name = 'land/land_detail.html'
    context_object_name = 'land'