# Generated by Django 2.2 on 2019-05-04 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0007_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='posted_in',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='photo.PhotoModel'),
        ),
    ]