from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'description', 'photo')
# class PostForm(forms.Form):
#     title = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Title', 'class': 'form-control', 'id': 'title', 'required': "true"}))
#     author = forms.CharField(widget = forms.TextInput(attrs={'placeholder': 'Author', 'class': 'form-control', 'id': 'name', 'required': "true"}))
#     description = forms.CharField(widget = forms.Textarea(attrs={'placeholder': 'Add Caption...', 'class': 'form-control', 'id': 'description', 'required': "true"}))
#     photo = forms.ImageField()
#     # class Meta:
#     #     model = Post
#     #     fields = ('photo')        