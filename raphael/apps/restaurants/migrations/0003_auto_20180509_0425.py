# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-05-09 04:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0002_auto_20180508_1349'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='restaurants',
            name='owner',
        ),
        migrations.AddField(
            model_name='restaurants',
            name='owner_id',
            field=models.PositiveIntegerField(default=0),
            preserve_default=False,
        ),
    ]
