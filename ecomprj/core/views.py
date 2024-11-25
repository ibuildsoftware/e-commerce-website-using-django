from django.shortcuts import render
from django.http import HttpResponse # added to avoid 'HttpResponse not defined' error
# Create your views here.

def index(request):
    return render(request, 'core/index.html')
