# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.validators import MinLengthValidator
from django.db import models
from django.contrib.auth.models import User

class Item(models.Model):
    name = models.CharField(max_length=30, unique=True, validators=[MinLengthValidator(3)])
    created_by = models.ForeignKey(User, related_name='item')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    users = models.ManyToManyField(User, related_name="items")

    def __str__(self):
        return self.name

