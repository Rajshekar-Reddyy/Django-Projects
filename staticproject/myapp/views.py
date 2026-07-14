from django.shortcuts import render

# Create your views here.
def myview(request):
    name="raj"
    animal="lion"
    bird="parrot"
    ctx={"name":name,"animal":animal,"bird":bird}
    return render(request,'fav.html',ctx)

