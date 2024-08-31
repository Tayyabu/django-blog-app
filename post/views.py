from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
# Create your views here.




def home(request):
  
    posts =Post.objects.filter(is_popular=True)
  
    return render(request,"index.html",{"posts":posts})

def all_posts(request):
  
     
    posts =Post.objects.all()
  
    return render(request,"all_posts.html",{"posts":posts})

    

def get_post_by_slug(request,slug):
    post =get_object_or_404(Post,slug=slug)
    return render(request,"post_page.html",{"post":post})
