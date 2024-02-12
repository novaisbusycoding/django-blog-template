from django.db import models
from ckeditor.fields import RichTextField

class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    biography = models.TextField()

    class Meta:
        verbose_name_plural = "authors"

    def __str__(self):
        return self.name
    
class Post(models.Model):
    # Main data
    title = models.CharField(max_length=255)
    description = models.CharField(max_length=160)
    body = RichTextField()
    authors = models.ManyToManyField("Author")
    categories = models.ManyToManyField("Category")

    # Auto-managed data
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "posts"

    def __str__(self):
        return self.title