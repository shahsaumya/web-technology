# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-01 13:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20170929_1317'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='user_ref_id',
            field=models.IntegerField(default=1),
        ),
    ]
