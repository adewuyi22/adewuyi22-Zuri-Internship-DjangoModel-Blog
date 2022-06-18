from django.db import models
from django.contrib.auth import get_user_model

# Create your models here.
class BlogPost(models.Model):
    class Meta:
        verbose_name = "Blog Post"
        verbose_name = "Blog Post"
    blog_title = models.CharField(max_length=200)
    blog_post = models.TextField()
    #blog_author =  models.CharField(max_length=50)
    blog_author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    Published_year = models.DateTimeField()
    
    
        
