# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-19 05:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mypeckyspace', '0006_auto_20180418_1852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='uploaded_file',
            field=models.FileField(default=None, upload_to='documents/'),
        ),
    ]
