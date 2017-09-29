# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-29 12:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movieId', models.CharField(default=None, max_length=5)),
                ('title', models.CharField(default=None, max_length=100)),
                ('genres', models.CharField(default=None, max_length=100)),
                ('imdbId', models.CharField(default=None, max_length=10)),
                ('tmdbId', models.CharField(default=None, max_length=10)),
            ],
        ),
    ]
