# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-05 01:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0007_blank_categories_20171101_1638'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='episodes',
            field=models.ManyToManyField(blank=True, to='data_models.Episode', verbose_name='Episoder'),
        ),
    ]
