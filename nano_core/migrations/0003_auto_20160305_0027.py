# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import stdimage.models


class Migration(migrations.Migration):

    dependencies = [
        ('nano_core', '0002_auto_20160122_1710'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='event',
            options={'verbose_name': 'event', 'verbose_name_plural': 'events'},
        ),
        migrations.AlterModelOptions(
            name='news',
            options={'verbose_name_plural': 'news'},
        ),
        migrations.AlterModelOptions(
            name='userprofile',
            options={'verbose_name': 'user profile', 'verbose_name_plural': 'user profiles'},
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='picture',
            field=stdimage.models.StdImageField(upload_to=b'profile_pictures', blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='user',
            field=models.OneToOneField(related_name='user_profile', primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL),
        ),
    ]
