from django.db import models
from django.contrib.auth.models import User
from PIL import Image
import uuid


class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        null=True, blank=True, upload_to='images/Profile_images')
    bio = models.CharField(max_length=250)

    def __str__(self):
        return str(self.user)

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.profile_pic.path)
        width, height = img.size  # Get dimensions

        if width > 300 and height > 300:
            # keep ratio but shrink down
            img.thumbnail((width, height))

        # check which one is smaller
        if height < width:
            # make square by cutting off equal amounts left and right
            left = (width - height) / 2
            right = (width + height) / 2
            top = 0
            bottom = height
            img = img.crop((left, top, right, bottom))

        elif width < height:
            # make square by cutting off bottom
            left = 0
            right = width
            top = 0
            bottom = width
            img = img.crop((left, top, right, bottom))

        if width > 150 and height > 150:
            img.thumbnail((150, 150))

        img.save(self.profile_pic.path)


class comments(models.Model):
    message = models.TextField(max_length=255)
    user = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user.pk)
