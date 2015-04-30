from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.ForeignKey(User)
    picture = models.ImageField(upload_to='profile_images', blank=True)
