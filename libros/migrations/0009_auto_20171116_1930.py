# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 01:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libros', '0008_auto_20171116_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prestamo',
            name='fecha_entrega',
            field=models.DateField(blank=True, null=True),
        ),
    ]
