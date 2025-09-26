from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User

class Post(models.Model):
    STATUS = (
        (0, "Rascunho"),
        (1, "Publicado")
    )

    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog_posts')  # <---
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)  # <---
    status = models.IntegerField(choices=STATUS, default=0)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title