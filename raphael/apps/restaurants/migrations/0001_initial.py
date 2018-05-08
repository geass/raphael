# -*- coding: utf-8 -*-
<<<<<<< HEAD
# Generated by Django 1.11.13 on 2018-05-08 13:47
=======
# Generated by Django 1.11.13 on 2018-05-08 14:17
>>>>>>> feature/oauth-implementation
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Restaurants',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(max_length=255, unique=True)),
                ('title', models.CharField(db_index=True, max_length=255)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='snippets', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'restaurants',
            },
        ),
    ]
