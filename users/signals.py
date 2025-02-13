from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from .models import Profile

# ========================== DISCLAIMER =============================
# Don't forget to add this:  
#   def ready(self):
#         import users.signals
# to class UsersConfig(AppConfig) in /users/apps.py

# User sends the signal and post_save is a signal that gets triggered whenever an 
# object is saved. So our goal is to get a post_save signal when a user is created.
# So here, User is going to send the signal and the receiver of the signal will be 
# the function we define below which gets the signal and then performs a task (which 
# is to automatically create a profile when a user is created). If we don't use signals,
# then the admin has to manually create a profile for every new account that registers to 
# the site

@receiver(post_save, sender=User) # the decorator has to specify as arguments what the signal is (post_save) and the sender (User) 
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()
