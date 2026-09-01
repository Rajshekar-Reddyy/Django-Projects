from django.urls import path
from . import views
from blog.views import *

urlpatterns=[
    # path('',views.home,name='home'),
    # path('blog/<int:id>/',views.post_detail,name='post_detail'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('about1/',AboutView.as_view(),name='aboutview'),
    path('',PostListView.as_view(),name='home'),
    path('blog/<int:pk>/',PostDetailView.as_view(),name='post_detail'),


]