# Generated by Django 2.2 on 2019-04-06 21:22

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0005_auto_20190407_0017'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photomodel',
            name='likes',
        ),
        migrations.AddField(
            model_name='photomodel',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
