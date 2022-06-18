from django.contrib import admin
from .models import BlogPost

# Register your models here.
class BlogPostDB(admin.ModelAdmin):
    list_display = [
        "blog_title", "blog_post", "blog_author", "Published_year"

    ]

admin.site.register(BlogPost, BlogPostDB)     