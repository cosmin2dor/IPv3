# Generated by Django 2.2 on 2019-04-20 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0014_auto_20190406_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=models.ImageField(blank=True, default='pics/default.png', upload_to='pics/'),
        ),
    ]
