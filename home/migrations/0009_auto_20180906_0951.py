# Generated by Django 2.0.7 on 2018-09-06 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0008_post_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
