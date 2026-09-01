from django.shortcuts import render,get_object_or_404
from .models import Post
from django.http import HttpResponse
from .forms import ContactForm
from django.views.generic import TemplateView,ListView,DetailView

# def home(request):
#     posts=Post.objects.all()

#     context={
#         "posts":posts
#     }

#     return render(request, 'home.html',context)

#TEMPLATE VIEW

class AboutView(TemplateView):
    template_name='about.html'
    

# LIST VIEW 
class PostListView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='posts'
#------------------------------------------------------------------------------------------

# def post_detail(request,id):
#     post=get_object_or_404(Post,id=id)

#     return render(request,'post_detail.html',{'post':post})

# DETAIL VIEW

class PostDetailView(DetailView):
    model=Post
    template_name='post_detail.html'
    context_object_name='post'




def about(request):
    return render(request,'about.html')

def contact(request):
    if request.method=='POST':
        form=ContactForm(request.POST) 
        if form.is_valid():
            context=form.cleaned_data
            return HttpResponse(f"Thank you,{context.get('name')}! Your message has been received.")
            
            
    else:
        form=ContactForm()
            

    return render(request,'contact.html',{'form':form})

