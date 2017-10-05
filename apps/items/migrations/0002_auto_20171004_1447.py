# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-04 21:47
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='name',
            field=models.CharField(max_length=30, unique=True, validators=[django.core.validators.MinLengthValidator(3)]),
        ),
    ]
