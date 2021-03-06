# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-01 16:15
from __future__ import unicode_literals

import django.utils.timezone
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0005_categories_20171101_1535'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='episode',
            options={'verbose_name': 'Episode', 'verbose_name_plural': 'Episoder'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Artikkel', 'verbose_name_plural': 'Artikler'},
        ),
        migrations.AlterModelOptions(
            name='show',
            options={'verbose_name': 'Program', 'verbose_name_plural': 'Programmer'},
        ),
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(verbose_name='Brødtekst'),
        ),
        migrations.AlterField(
            model_name='post',
            name='created_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='publications', to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av'),
        ),
        migrations.AlterField(
            model_name='post',
            name='deleted',
            field=models.BooleanField(default=False, verbose_name='Slettet'),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='uploads/images', verbose_name='Bilde'),
        ),
        migrations.AlterField(
            model_name='post',
            name='lead',
            field=models.CharField(max_length=140, verbose_name='Ingress'),
        ),
        migrations.AlterField(
            model_name='post',
            name='publish_at',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Publisert'),
        ),
        migrations.AlterField(
            model_name='post',
            name='show',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='data_models.Show', verbose_name='Program'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=64, verbose_name='Tittel'),
        ),
        migrations.AlterField(
            model_name='show',
            name='archived',
            field=models.BooleanField(default=False, verbose_name='Arkivert'),
        ),
        migrations.AlterField(
            model_name='show',
            name='content',
            field=models.TextField(verbose_name='Lang beskrivelse'),
        ),
        migrations.AlterField(
            model_name='show',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL, verbose_name='Opprettet av'),
        ),
        migrations.AlterField(
            model_name='show',
            name='image',
            field=models.ImageField(upload_to='uploads/images', verbose_name='Programlogo'),
        ),
        migrations.AlterField(
            model_name='show',
            name='lead',
            field=models.CharField(max_length=140, verbose_name='Kort beskrivelse'),
        ),
        migrations.AlterField(
            model_name='show',
            name='name',
            field=models.CharField(max_length=64, unique=True, verbose_name='Navn'),
        ),
    ]
