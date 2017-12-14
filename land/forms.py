from django import forms
from .models import Land
from searchableselect.widgets import SearchableSelect
class CreateForm(forms.Form):
    name = forms.CharField()
    other_attributes = forms.CharField(widget=forms.Textarea(),required=False)
    government_private_key = forms.CharField(widget=forms.PasswordInput)

class TransferForm(forms.Form):
    asset = forms.ModelChoiceField(queryset=Land.objects.all(), widget=forms.Select(attrs={'class':'form-control input-sm'}))
    owner_private_key = forms.CharField(widget=forms.PasswordInput)
    price = forms.IntegerField()
    receipient_public_key = forms.CharField()
    

class RegisterForm(forms.Form):
    name = forms.CharField()
    public_key = forms.CharField()