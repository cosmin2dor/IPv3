from django.contrib import admin
from .models import PhotoModel, Comment

admin.site.register(PhotoModel)
admin.site.register(Comment)
