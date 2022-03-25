# <app>/signals.py:

from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.core.mail import send_mail
from .models import ChatGroup


@receiver(post_save, sender=User)
def send_email_to_admin(sender, instance, created, **kwargs):
    if created:
        print("new user crated", instance)
        for i in User.objects.all().exclude(username=instance):
            print(i)
            chat_group = ChatGroup.objects.get_or_create(name=str(instance) + '-' + str(i.username))
            print(chat_group[0])
            chat_group[0].user_set.add(i)
            chat_group[0].user_set.add(instance)