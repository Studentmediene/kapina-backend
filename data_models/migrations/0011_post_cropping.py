# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-01-31 20:30
from __future__ import unicode_literals

from django.db import migrations
import sorl_cropping.fields


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0010_merge_20171113_2120'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='cropping',
            field=sorl_cropping.fields.ImageRatioField(blank=True, help_text='Velg bildeutsnitt', image_field='image', max_length=255, size='1024x567', verbose_name='Bildeutsnitt'),
        ),
    ]
