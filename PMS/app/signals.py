from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile, Project

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance, first_name=instance.first_name, last_name=instance.last_name, email=instance.email)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    try:
        instance.profile.save()
    except Profile.DoesNotExist:
        # Handle the case where the profile does not exist
        pass

@receiver(post_save, sender=Project)
def project_created_msg(sender, instance, **kwargs):
    print(f"Welcome {instance.owner}! You have created a project.")
    # You can add your email-sending logic here