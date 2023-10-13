from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import *
from django.views.generic import ListView, DetailView, CreateView
from .models import *

class PhoneView(ListView):
    model = Phone
    template_name = 'home.html'
    
class CreatePhone(CreateView):
    model = Phone
    form_class = PhoneForm
    template_name = 'create.html'
    success_url = reverse_lazy('home')

class XiaomiView(ListView):
    model = Phone
    template_name = 'xiaomi.html'