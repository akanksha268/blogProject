# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2021-04-21 14:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media/profile_pics'),
        ),
    ]
