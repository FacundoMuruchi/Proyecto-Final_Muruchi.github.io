from django import forms
from .models import Post

class UserForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(max_value=99, required=False)
    email = forms.EmailField(max_length=256, required=False)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['name','author','text','post']