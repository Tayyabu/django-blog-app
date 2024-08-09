
from . import views

from django.conf.urls.static import static

from app import settings 

from django.urls import path

urlpatterns = [
  path("",views.home,name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
