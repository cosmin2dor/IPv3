# Generated by Django 2.2 on 2019-04-06 16:03

from django.db import migrations
import sorl.thumbnail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20190406_0412'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='profile_picture',
            field=sorl.thumbnail.fields.ImageField(blank=True, default='pics/default.png', upload_to='pics/'),
        ),
    ]
