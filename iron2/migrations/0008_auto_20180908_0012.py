# Generated by Django 2.0.7 on 2018-09-07 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('iron2', '0007_auto_20180831_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(default='profile_image/elder.JPG', upload_to='profile_image'),
        ),
    ]