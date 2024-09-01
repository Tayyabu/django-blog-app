
from . import views





from django.urls import path

urlpatterns = [
  path("",views.home,name="home"),
  path("posts/all",views.blogs,name="blogs"),
  path("posts/<str:slug>",views.get_post_by_slug,name="post"),
  path('search/',views.search,name='search')
] 


