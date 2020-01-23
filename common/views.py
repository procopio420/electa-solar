# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.shortcuts import render
from services.models import Service
# Create your views here.

def send_email(request):
    send_mail('Subject here',
        'Here is the message.', 
        'lucas.p@ges.inatel.br',
        ['lucas.p@ges.inatel.br'],
    )

def index(request):
    services = Service.objects.all()
    return render(request, 'common/index.html', {'services':services})