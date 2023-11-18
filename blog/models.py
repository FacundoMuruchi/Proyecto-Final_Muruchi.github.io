from django.db import models
from ckeditor.fields import RichTextField

class Usuario(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField(null=True, blank=True)
    email = models.EmailField(max_length=254,null=True, blank=True)

    def __str__(self):
        return f"{self.surname}, {self.name}"
    
class Post(models.Model):
    name = models.CharField(max_length=128)
    author = models.CharField(max_length=50)
    text = RichTextField(max_length=5000)
    post = models.IntegerField(choices=[
        (1, "Story"),
        (2, "Poem")
    ],
    default=1)
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        if self.post == 1:
            return f"{self.name}, {self.author} (Story)"
        else:
            return f"{self.name}, {self.author} (Poem)"