from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=50, required=True)
    surname = forms.CharField(max_length=50, required=True)
    password = forms.CharField(max_length=50, required=True)
    age = forms.IntegerField(max_value=99, required=False)
    email = forms.EmailField(max_length=256, required=False)

class PoemForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    author = forms.CharField(max_length=50, required=True)
    text = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)
    
class StoryForm(forms.Form):
    name = forms.CharField(max_length=128, required=True)
    author = forms.CharField(max_length=50, required=True)
    text = forms.CharField(max_length=5000, required=True, widget=forms.Textarea)