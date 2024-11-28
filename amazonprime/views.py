from django.shortcuts import render
from django.http import HttpResponse
def webtv(request):
    return HttpResponse('<h1>This app is used to watch latest web series and movies</h1>')

# Create your views here.
