# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-05-25 03:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('principal', '0020_alumno_clases'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumno',
            name='Clases',
            field=models.ManyToManyField(related_name='tomadas', to='principal.Clase'),
        ),
    ]