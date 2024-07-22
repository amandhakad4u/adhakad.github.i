
from django.shortcuts import render, HttpResponse, redirect;
# Create your views here.
from .models import users




def home (request) :

    return render (request, 'home.html')

def contact (request) :

    return render (request, 'contact.html')




