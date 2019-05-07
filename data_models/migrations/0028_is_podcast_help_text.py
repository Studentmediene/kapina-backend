# Generated by Django 2.0.12 on 2019-05-07 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_models', '0027_update_podcast_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='is_podcast',
            field=models.BooleanField(default=False, help_text='Podkaster får lenke til podkast-feeden, og (etterhvert) mulighet til å legge inn podkast-episoder.', verbose_name='Programmet er en podkast'),
        ),
    ]
