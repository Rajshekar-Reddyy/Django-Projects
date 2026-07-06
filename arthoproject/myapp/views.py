from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def add(request):
    a=int(input("enter a number"))
    b=int(input("enter a second number"))
    c=a+b
    return HttpResponse(str(c))

def sub(request):
    a=int(input("enter a number"))
    b=int(input("enter a second number"))
    c=a-b
    return HttpResponse(str(c))

def mul(request):
    a=int(input("enter a number"))
    b=int(input("enter a second number"))
    c=a*b
    return HttpResponse(str(c))

def div(request):
    a=int(input("enter a number"))
    b=int(input("enter a second number"))
    c=a/b
    return HttpResponse(str(c))