# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-08-18 04:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('menus', '0006_auto_20170818_0716'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menuitem',
            name='explicit_url',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
