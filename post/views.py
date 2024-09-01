from django.http import HttpResponse
from django.shortcuts import render,get_object_or_404
from .models import Post
from django.db.models import Q
# Create your views here.




def home(request):
  
    posts =Post.objects.filter(is_popular=True)
  
    return render(request,"index.html",{"posts":posts})

def blogs(request):
  
     
    posts =Post.objects.all()
  
    return render(request,"all_posts.html",{"posts":posts})

    

def get_post_by_slug(request,slug):
    post =get_object_or_404(Post,slug=slug)
    return render(request,"post_page.html",{"post":post})


def search(request):
    search_text= request.GET['search']
    posts = Post.objects.filter(Q(title__icontains=search_text)| Q(intro__icontains=search_text)|Q(content__icontains=search_text))
    if len(posts)>0:
        return render(request,'search.html',{'posts':posts})
    return render(request,'search.html')