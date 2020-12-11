# Generated by Django 3.1.4 on 2020-12-10 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtubers', '0006_auto_20201210_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='youtuber',
            name='camera_type',
            field=models.CharField(choices=[('canon', 'canon'), ('fuji', 'fuji'), ('sony', 'sony'), ('other', 'other'), ('red', 'red'), ('panasonic', 'panasonic'), ('nikon', 'nikon')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='category',
            field=models.CharField(choices=[('vlogs', 'vlogs'), ('cooking', 'cooking'), ('comdey', 'comdey'), ('mobile_review', 'mobile_review'), ('gaming', 'gaming'), ('film_making', 'film_making'), ('code', 'code')], max_length=255),
        ),
        migrations.AlterField(
            model_name='youtuber',
            name='crew',
            field=models.CharField(choices=[('solo', 'solo'), ('small', 'small'), ('large', 'large')], max_length=255),
        ),
    ]
