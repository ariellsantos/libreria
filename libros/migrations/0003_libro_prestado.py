# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 01:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0002_auto_20171116_1737'),
    ]

    operations = [
        migrations.AddField(
            model_name='libro',
            name='prestado',
            field=models.BooleanField(default=False),
        ),
    ]
