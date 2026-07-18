from django.shortcuts import render
from myapp.models import Student

# Create your views here.
def studview(request):
    s=Student.objects.all()
    ctx={'stud':s}
    return render(request,'stud.html',ctx)

