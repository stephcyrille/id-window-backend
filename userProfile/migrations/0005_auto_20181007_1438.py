# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-07 13:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userProfile', '0004_useragent_agent'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useragent',
            name='language',
            field=models.CharField(default='fr', max_length=12),
        ),
    ]
