from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from cloudinary.models import CloudinaryField


# Create your models here

class Post(models.Model):
    title = models.CharField(max_length =50,unique=True)
    intro =models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(default ="",blank=True,null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,related_name ="posts")
    def partial_intro(self):
        return self.intro[:100]

    def __str__(self):
        return self.title


class Section(models.Model):
    subtitle = models.CharField(max_length=50,unique=True)
    paragraph = models.TextField()
    image= CloudinaryField('image',null=True,blank=True)
    post = models.ForeignKey(Post,on_delete=models.CASCADE,related_name ="sections")
    created_at =models.DateTimeField(auto_now_add =True)
    def __str__(self) -> str:
        return f"{self.subtitle} of post \"{self.post.title}\""
    
    class Meta:
        ordering = ("-created_at",)
    





def post_created(sender,instance,created, **kwargs):
    if created:
        instance.slug = instance.title.replace(" ","-")
        instance.save()



post_save.connect(post_created,sender=Post)   








