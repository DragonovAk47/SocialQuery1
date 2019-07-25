# Generated by Django 2.0.7 on 2018-09-18 10:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('iron2', '0011_auto_20180913_0245'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='document',
            name='description',
        ),
        migrations.RemoveField(
            model_name='document',
            name='image',
        ),
        migrations.AddField(
            model_name='document',
            name='file_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=255),
            preserve_default=False,
        ),
    ]