from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(
        upload_to="profile_images/", default="default.png"
    )
    bio = models.TextField(blank=True)

    def __str__(self):
        return self.user.username
