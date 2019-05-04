from .models import PhotoModel, Comment
from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('image_url', 'description', 'keywords',)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)
