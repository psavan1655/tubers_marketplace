from django.db import models

# Create your models here.

class Team(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    role = models.CharField(max_length=100)
    fb_link = models.CharField(max_length=255)
    insta_link = models.CharField(max_length=255)
    yt_link = models.URLField(max_length=200, default="https://www.youtube.com/channel/UC2kNKznWzLNC0R6BeHa6m4g?sub_confirmation=1")
    photo = models.ImageField(upload_to='media/team/%Y/%m/%d/')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.first_name

class Slider(models.Model):
    headline = models.CharField(max_length=255)
    subtitle = models.CharField(max_length=255)
    button_text = models.CharField(max_length=255)
    button_link = models.URLField(max_length=200, default="https://psavan1655.github.io/savanpatel.github.io/")
    photo = models.ImageField(upload_to='media/slider/%Y/')  #%m can be added for month wise folder in database.
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.headline