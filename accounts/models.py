from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):

    user = models.OneToOneField(User)

    about = models.CharField(max_length = 225,blank = True)
    # pip install pillow to use this!
    profile_pic = models.ImageField(upload_to="media/profile_pics", blank=True)

    def __str__(self):
        return self.user.username
