# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 22:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0003_auto_20171004_1502'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
