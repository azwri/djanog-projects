from django.dispatch import receiver
from django.db.models.signals import post_save
from django.contrib.auth import get_user_model
from .models import  Profile

User = get_user_model()


@receiver(post_save, sender=User)
def user_postsave(sender, instance, created, **kwargs):
    user = instance
    if created:
        Profile.objects.create(user=user)