# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=305)
    text = models.TextField()
    image = models.ImageField(null=True, blank=True, upload_to='images/')
    icon = models.FileField(null=True, blank=True, upload_to='icons/')
    icon2 = models.FileField(null=True, blank=True, upload_to='icons/')
