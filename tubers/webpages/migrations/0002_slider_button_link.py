# Generated by Django 3.1.4 on 2020-12-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='button_link',
            field=models.URLField(default='https://psavan1655.github.io/savanpatel.github.io/'),
        ),
    ]