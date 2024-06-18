# blog/models.py
from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser, Group, Permission

class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = models.TextField()
    date_posted = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class UserProfile(AbstractUser):
    profile_photo = models.ImageField(upload_to='profile_photos/', blank=True, null=True)
    groups = models.ManyToManyField(Group, related_name='user_profiles')  # Add related_name
    user_permissions = models.ManyToManyField(Permission, related_name='user_profiles')  # Add related_name

    def __str__(self):
        return self.username
