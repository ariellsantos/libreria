# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-16 23:37
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='libro',
            old_name='categora',
            new_name='categoria',
        ),
    ]
