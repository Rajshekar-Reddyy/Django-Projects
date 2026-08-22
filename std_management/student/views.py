from django.shortcuts import render
from .details import STUDENTS

# Create your views here.
def home(request):
    context={"students":STUDENTS}

    
    return render(request,'home.html',context)

def blog(request,id):
    context={}
    for student in STUDENTS:
        if id==student['roll_no']:
            context['student']=student
            break
    else:
        context['message']="student_not_found"
    return render(request,'display.html',context)
