from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    email=models.EmailField(max_length=30,blank=False,null=False)
    mobile=models.CharField(max_length=13)
    address=models.CharField(max_length=100)
    active=models.BooleanField(default=True)


    def __str__(self):
        return self.user.username




@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
    instance.profile.save()