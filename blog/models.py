from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
    
class Post(models.Model):
    title = models.CharField(max_length=128)
    text = RichTextField(max_length=5000)
    post = models.IntegerField(choices=[
        (1, "Story"),
        (2, "Poem")
    ])
    date = models.DateTimeField(auto_now=True)
    creator = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        if self.post == 1:
            return f"{self.title}, {self.creator} (Story)"
        else:
            return f"{self.title}, {self.creator} (Poem)"