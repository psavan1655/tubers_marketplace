# Generated by Django 3.1.4 on 2020-12-08 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpages', '0003_auto_20201208_1827'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='yt_link',
            field=models.URLField(default='https://www.youtube.com/channel/UC2kNKznWzLNC0R6BeHa6m4g?sub_confirmation=1'),
        ),
    ]
