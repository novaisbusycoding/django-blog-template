from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=55)
    description = models.CharField(max_length=255)

class Author(models.Model):
    name = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    biography = models.TextField()

    def __str__(self):
        return self.nome
    
class Post(models.Model):
    # Main data
    title = models.CharField(max_length=255)
    body = models.TextField()
    authors = models.ManyToManyField("Author")
    categories = models.ManyToManyField("Category")

    # Auto-managed data
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)