from django.shortcuts import render
from api.models import *
from .forms import *
from django.views.generic import CreateView
from django.urls import reverse_lazy

# Create your views here.

class UserReigtrationView(CreateView):
    template_name = 'register.html'
    form_class = UserRegistrationForm
    success_url = reverse_lazy('sign-up')



