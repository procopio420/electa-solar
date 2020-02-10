# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Application

# Create your views here.
def apps(request):
    apps = Application.objects.all()
    return render(request, 'apps/apps.html', {'apps':apps})