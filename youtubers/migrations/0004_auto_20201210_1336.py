# Generated by Django 3.1.4 on 2020-12-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0003_auto_20201210_1052'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('panasonic', 'panasonic'), ('other', 'other'), ('nikon', 'nikon'), ('canon', 'canon'), ('red', 'red'), ('sony', 'sony'), ('fuji', 'fuji')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('cooking', 'cooking'), ('gaming', 'gaming'), ('comdey', 'comdey'), ('film_making', 'film_making'), ('mobile_review', 'mobile_review'), ('code', 'code'), ('vlogs', 'vlogs')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('large', 'large'), ('small', 'small')], max_length=255),
        ),
    ]
