from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField
from tinymce import models as md

# Create your models here

class Post(models.Model):
    title = models.CharField(max_length =50,unique=True)
    intro = models.TextField()
    content = md.HTMLField(null=True,blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default ="",blank=True,null=True)
    is_popular = models.BooleanField(default=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name ="posts")
   
    def partial_intro(self):
        return f'{self.intro[:30]}...'

    def __str__(self):
        return self.title



class BlogImage(models.Model):
    image =CloudinaryField()
    posts =models.ManyToManyField(Post,related_name="images")



def post_created(sender,instance,created, **kwargs):
    if created:
        instance.slug = instance.title.replace(" ","-")
        instance.save()



post_save.connect(post_created,sender=Post)   








