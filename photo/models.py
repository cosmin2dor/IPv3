from django.db import models
from users.models import CustomUser


class PhotoModel(models.Model):
    image_url = models.ImageField(upload_to='uploads/', blank=False, null=False)
    description = models.CharField(max_length=200, blank=True)
    likes = models.ManyToManyField(CustomUser, blank=True, related_name='post_likes')
    keywords = models.CharField(max_length=500, blank=True)
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now=False, auto_now_add=True)

