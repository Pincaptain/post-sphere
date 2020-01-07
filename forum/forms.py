from django.forms import ModelForm, Textarea, TextInput, SelectMultiple

from .models import Thread, Post, Comment


class ThreadForm(ModelForm):
    class Meta:
        model = Thread
        fields = ['name', 'description', 'rules']
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'rules': SelectMultiple(attrs={'class': 'custom-select'}),
        }


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'tags']
        widgets = {
            'title': TextInput(attrs={'class': 'form-control'}),
            'description': Textarea(attrs={'class': 'form-control'}),
            'tags': SelectMultiple(attrs={'class': 'custom-select'}),
        }


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['comment']
        widgets = {
            'comment': Textarea(attrs={'class': 'form-control'}),
        }
