# from django import forms
from django.forms import ModelForm
from .models import Post, Comment
from django.utils.translation import gettext_lazy as _

class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'body']
        

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body')
        help_texts = {
            'name': _('Some useful help text'),
        }