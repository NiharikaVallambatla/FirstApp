# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class persons(models.Model):
    name = models.CharField(default='Nikki',max_length=255)

    def __str__(self):
        return self.name

class thing_list(models.Model):
    title=models.TextField()
    person = models.ForeignKey(persons)
    fromHome=models.BooleanField(default=True)

    def __str__(self):
        return self.title