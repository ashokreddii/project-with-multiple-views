from django.shortcuts import render
from django.http import HttpResponse
def payment(request):
    return HttpResponse('<h1>This app is to perform payments with the help of mobile</h1>')

# Create your views here.
