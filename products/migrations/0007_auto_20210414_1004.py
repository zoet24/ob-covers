# Generated by Django 3.1.7 on 2021-04-14 10:04

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0006_auto_20210413_1542'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colour',
            name='rgb_background',
        ),
        migrations.RemoveField(
            model_name='colour',
            name='rgb_border',
        ),
        migrations.RemoveField(
            model_name='colour',
            name='rgb_colour',
        ),
        migrations.AddField(
            model_name='colour',
            name='hex_background',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='colour',
            name='hex_border',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
        migrations.AddField(
            model_name='colour',
            name='hex_colour',
            field=colorfield.fields.ColorField(default='#FFFFFF', max_length=18),
        ),
    ]