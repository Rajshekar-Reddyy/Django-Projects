from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view2(request):
    b="second app2"
    return httpresponse(b)
