from django import forms

class CreateForm(forms.Form):
    name = forms.CharField()
    other_attributes = forms.CharField(widget=forms.Textarea(),required=False)
    government_private_key = forms.CharField(widget=forms.PasswordInput)

class TransferForm(forms.Form):
    asset_id = forms.CharField()
    owner_private_key = forms.CharField(widget=forms.PasswordInput)
    receipient_public_key = forms.CharField()

class RegisterForm(forms.Form):
    name = forms.CharField()
    public_key = forms.CharField()