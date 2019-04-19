from .models import PhotoModel
from django import forms


class PhotoForm(forms.ModelForm):
    class Meta:
        model = PhotoModel
        fields = ('image_url', 'description', 'keywords',)
