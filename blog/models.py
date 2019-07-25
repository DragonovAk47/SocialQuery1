from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Blog(models.Model):
    news_type=(
        ('Finance','Finance'),
        ('Education', 'Education'),
        ('Entertainment', 'Entertainment'),
        ('General', 'General'),
    )
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=50,default="")
    Heading=models.CharField(max_length=50,default="")
    Picture=models.ImageField(upload_to="blog_pictures",null=True)
    Blog=models.CharField(max_length=250,default="")
    date=models.DateTimeField(auto_now_add=True)
    type = models.CharField(max_length=13, choices=news_type)
