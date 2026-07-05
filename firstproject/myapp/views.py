from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def view1(request):
    a="welcome to django sesioon.."
    return HttpResponse(a)

def view2(request):
    b="hi i am rajshekar"
    return HttpResponse(b)