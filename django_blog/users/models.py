from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    status = models.CharField(max_length=200, blank=True)

    def __str__(self):
        return f'{self.user.username} Profile'

    # Scale image before upload
    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)


class UserFollower(models.Model):
    following = models.OneToOneField(
        Profile, on_delete=models.CASCADE, related_name="following")
    followers = models.ForeignKey(
        Profile, on_delete=models.CASCADE, related_name="followers",   blank=True)
