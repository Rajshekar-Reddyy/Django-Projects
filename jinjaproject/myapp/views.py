from django.shortcuts import render

# Create your views here.
def view1(request):
    name="rama"
    place="banaglaore"
    ctx={'name':name,'place':place}
    return render(request,'my.html',ctx)



