# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('start', models.DateTimeField(blank=True)),
                ('end', models.DateTimeField(blank=True)),
                ('description', models.TextField()),
                ('place', models.CharField(max_length=100, blank=True)),
                ('url', models.CharField(max_length=200, blank=True)),
                ('image', models.FileField(upload_to=b'news_image', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50)),
                ('content', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(upload_to=b'news_image', blank=True)),
            ],
            options={
                'verbose_name_plural': 'stories',
            },
        ),
        migrations.CreateModel(
            name='Publication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=1000)),
                ('authors', models.CharField(max_length=1000)),
                ('content', models.TextField()),
                ('date', models.IntegerField(max_length=4)),
                ('pdf', models.FileField(upload_to=b'publication_pdf', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('user', models.OneToOneField(primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('position', models.CharField(default=b'UNDEF', max_length=20, choices=[(b'UNDEF', b'undefined'), (b'PHD', b'phd_student'), (b'MSC', b'msc_student'), (b'ENG', b'research_engineer'), (b'ENG_ASST', b'assistant_engineer'), (b'PROF_ASST', b'assistant_professor'), (b'PROF', b'full_professor'), (b'MD', b'medical_doctor')])),
                ('phone', models.CharField(max_length=20, blank=True)),
                ('fax', models.CharField(max_length=20, blank=True)),
                ('address', models.CharField(max_length=50, blank=True)),
                ('bio', models.CharField(max_length=1000, blank=True)),
                ('picture', models.FileField(upload_to=b'profile_pictures', blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='publication',
            name='owners',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterUniqueTogether(
            name='publication',
            unique_together=set([('title', 'date', 'authors')]),
        ),
    ]
