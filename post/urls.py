
from . import views





from django.urls import path

urlpatterns = [
  path("",views.home,name="home"),
  path("posts/<str:slug>",views.get_post_by_slug,name="post"),
  path("posts/all",views.all_posts,name="all_posts"),
] 


