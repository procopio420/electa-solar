# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import Service
# Create your views here.

def service(request, pk):
    service = get_object_or_404(Service, pk=pk)
    services = Service.objects.all()
    return render(request, 'services/service.html', {'service':service,'services':services})