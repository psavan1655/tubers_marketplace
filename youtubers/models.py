from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Youtuber(models.Model):

    crew_choices = {
        ('solo', 'solo'),
        ('small', 'small'),
        ('large', 'large'),
    }

    camera_choices = {
        ('canon', 'canon'),
        ('nikon', 'nikon'),
        ('sony', 'sony'),
        ('red', 'red'),
        ('fuji', 'fuji'),
        ('panasonic', 'panasonic'),
        ('other', 'other'),
    }

    category_choices = {
        ('code', 'code'),
        ('mobile_review', 'mobile_review'),
        ('vlogs', 'vlogs'),
        ('comdey', 'comdey'),
        ('gaming', 'gaming'),
        ('film_making', 'film_making'),
        ('cooking', 'cooking'),
    }

    name = models.CharField(max_length=255)
    description = RichTextField()
    age = models.IntegerField()
    height = models.IntegerField()
    city = models.CharField(max_length=255)
    price = models.IntegerField()
    category = models.CharField(choices=category_choices, max_length=255)
    camera_type = models.CharField(choices=camera_choices, max_length=255)
    crew = models.CharField(choices=crew_choices, max_length=255)
    photo = models.ImageField(upload_to="media/ytubers/%Y/%m/")
    video_url = models.CharField(max_length=255)
    subs_count = models.CharField(max_length=255)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(auto_now_add=True)