from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='profile')
    picture = models.ImageField(upload_to='images/', blank=True, null=True)
