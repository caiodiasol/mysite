from django.contrib import admin

# Register your models here.

from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author', 'created_at')
    search_fields = ['title', 'content']
    list_filter = ('created_at', 'author', 'title')
    

admin.site.register(Post, PostAdmin)