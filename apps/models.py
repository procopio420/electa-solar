# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Application(models.Model):
    title = models.CharField(max_length=150)
    icon = models.FileField(upload_to='icons/')
    modal = models.CharField(max_length=150)