from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile


@receiver(post_save, sender=User) #when a user is saved, send this signal

def create_profile(sender, instance,created,**kwargs): #receiver is received by this function
    if created: #if user is created then create profile object
        Profile.objects.create(user =instance)


@receiver(post_save, sender=User) #when a user is saved, send this signal
def save_profile(sender, instance,**kwargs): # **kwargs accepts any additional keyword
    instance.profile.save()