from django.shortcuts import render
from django.http import HttpResponse
def items(request):
    return HttpResponse('<h1>with the help of this grocery app we can order grocery items related to kitchen and home</h1>')


# Create your views here.
