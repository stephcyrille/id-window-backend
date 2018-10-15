# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2018-10-07 13:34
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference', models.CharField(max_length=12)),
                ('role', models.CharField(max_length=12)),
                ('postOffice', models.CharField(max_length=150)),
                ('language', models.CharField(default='fr', max_length=2)),
                ('user', models.ForeignKey(on_delete='id', to=settings.AUTH_USER_MODEL, to_field=True)),
            ],
        ),
    ]
