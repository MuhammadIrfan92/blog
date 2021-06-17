from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
# Create your models here.
#C:\Users\Muhammad Irfan\Desktop\Web DEv\blog\blog>
STATUS  = (
    (0,"Draft"),
    (1,"Publish")
)

class test(models.Model):
    name = models.CharField(max_length=100,null=True)


class Post(models.Model):
    title = models.CharField(max_length= 200, null= True)
    slug = models.SlugField(max_length= 200, null= True)
   # author = models.ForeignKey(User, on_delete=CASCADE, related_name='blog_posts',null=True)
    author = models.CharField(max_length=100, null=True)
    updated_on = models.DateTimeField(auto_now=True,null=True)
    content = models.TextField(null=True)
    category = models.CharField(max_length=200, null = True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS,default=0,null=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title