from django.shortcuts import render

# Create your views here.

def index(reqeuest):
    return render(reqeuest, 'appone/index.html')