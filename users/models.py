from django.db import models
from django.contrib.auth.models import AbstractUser
from sorl.thumbnail import ImageField


class CustomUser(AbstractUser):
    profile_picture = ImageField(upload_to='pics/', default='pics/default.png', blank=True)
    birthday = models.DateField(blank=False, default="1999-01-01")

    def __str__(self):
        return self.username
