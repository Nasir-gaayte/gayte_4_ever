from django import forms
from .models import PostModel, CommentModel





class PostForm(forms.ModelForm):
    class Meta:
        model= PostModel
        fields = ("title", "head_image", "user", "category", "text")






class CommentForm(forms.ModelForm):
    
    class Meta:
        model= CommentModel
        fields = ( "name", "comm")