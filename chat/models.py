from django.db import models
from django.contrib.auth.models import Group


# Create your models here.
class ChatGroup(Group):
    """ extend Group model to add extra info"""
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('chat:room', args=[str(self.id)])
