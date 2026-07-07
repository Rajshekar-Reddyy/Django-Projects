from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view2(request):
    a="<h1/>this is the response from secondapp"
    return HttpResponse(a)
