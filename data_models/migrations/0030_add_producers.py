# Generated by Django 2.0.12 on 2020-02-04 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0029_post_image_credits'),
    ]

    operations = [
        migrations.AddField(
            model_name='settings',
            name='cultural_producer',
            field=models.CharField(default='', max_length=128, verbose_name='Kulturprodusent'),
        ),
        migrations.AddField(
            model_name='settings',
            name='entertainment_producer',
            field=models.CharField(default='', max_length=128, verbose_name='Underholdningsprodusent'),
        ),
    ]
