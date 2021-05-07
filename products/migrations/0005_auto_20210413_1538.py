# Generated by Django 3.1.7 on 2021-04-13 15:38

import colorful.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_colour_hex_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='colour',
            name='hex_code',
        ),
        migrations.AddField(
            model_name='colour',
            name='rgb_code',
            field=colorful.fields.RGBColorField(default='0,0,0'),
        ),
    ]