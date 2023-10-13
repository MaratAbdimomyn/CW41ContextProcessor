from django import forms
from django.forms import ModelForm
from .models import *

class PhoneForm(forms.ModelForm):
    
    class Meta:
        model = Phone
        fields = ('brand', 'name', 'color')