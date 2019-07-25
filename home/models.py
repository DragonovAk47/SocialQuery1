from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Post(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    caption=models.CharField(max_length=50,default="")
    Heading=models.CharField(max_length=50,default="")
    Picture=models.ImageField(upload_to="blog_pictures",null=True)
    date=models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.post
class Picture(models.Model):
    image=models.ImageField(upload_to='profile_image', default='index.JPG')
    user = models.ForeignKey(User,on_delete=models.PROTECT)

class Friend(models.Model):
    users=models.ManyToManyField(User)
    current_user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="owner",null=True)

    @classmethod
    def add_friend(cls,current_user,new_friend):
        friend,created=cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.add(new_friend)

    @classmethod
    def lose_friend(cls, current_user, new_friend):
        friend, created = cls.objects.get_or_create(
            current_user=current_user
        )
        friend.users.remove(new_friend)