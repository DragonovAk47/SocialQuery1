from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
# Create your models here.

class UserModelManager(models.Manager):
    def get_queryset(self):
       queryset=super(UserModelManager, self).get_queryset()
       return queryset

class Document(models.Model):

    Filename = models.CharField(max_length=255, blank=False)
    file=models.FileField(upload_to='files/',null=True)


class UserProfile(models.Model):
  
    user =models.OneToOneField(User,on_delete=models.CASCADE)
    School = models.CharField(max_length=100, default='')
    Status= models.CharField(max_length=100,default='')
    HomeTown= models.CharField(max_length=100, default='')
    High_School = models.CharField(max_length=100, default='')
    Looking_For= models.CharField(max_length=100, default='')
    Interested_In= models.CharField(max_length=100, default='')
    Political_Views= models.CharField(max_length=100, default='')
    Interests= models.CharField(max_length=100, default='')
    Clubs_and_Jobs= models.CharField(max_length=100, default='')
    Favorite_Movies= models.CharField(max_length=100, default='')
    Name = models.CharField(max_length=100, default='')
    Email = models.EmailField()
    description = models.CharField(max_length=100, default='')
    Mobile= models.IntegerField(default='00')
    Website = models.URLField()
    sexes = {('m','Male'),('f','Female'),('o','Other')}
    relationship_status = models.CharField(max_length = 10,default = "Not filled")
    religion = models.CharField(max_length = 20,default = "Not filled")
    sex = models.CharField(choices = sexes,max_length = 20,default = "Not filled")
    image=models.ImageField(upload_to='profile_image',default='profile_image/elder.JPG')
    objects=models.Manager()


    def __str__(self):
        return "%s's profile" % self.user.username.lstrip('profile')


def create_profile(sender,instance,created,**kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(create_profile,sender=User)


