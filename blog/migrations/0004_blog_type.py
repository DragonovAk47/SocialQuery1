# Generated by Django 2.0.7 on 2018-09-18 09:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blog_caption'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='type',
            field=models.CharField(default='', max_length=13),
        ),
    ]
