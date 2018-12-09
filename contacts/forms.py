from django import forms
from django.forms import TextInput, HiddenInput


class ContactForm(forms.Form):
    user_id = forms.CharField(widget=HiddenInput(attrs={'class' : 'form-control'}))
    listing_id = forms.CharField(widget=HiddenInput(attrs={'class' : 'form-control'}))
    listing = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
    name = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
    email = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
    phone = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
    message = forms.CharField(widget=TextInput(attrs={'class' : 'form-control'}))
