# Generated by Django 2.0.12 on 2019-04-28 16:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0024_populate_show_digas_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='show',
            name='is_podcast',
            field=models.BooleanField(default=False, verbose_name='Programmet er en podkast'),
        ),
    ]
