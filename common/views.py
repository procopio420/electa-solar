# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.mail import send_mail
from django.shortcuts import render
from services.models import Service
from .forms import QuoteForm
# Create your views here.

def index(request):
    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            lname = form.cleaned_data['lname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            obs = form.cleaned_data['obs']

            subject = 'New quote from electasolar.com'
            message = 'Name: '+name+' '+lname+'\n'+'Phone: '+phone+'\n'+'Email: '+email+'\n'+'Address: '+address+'\n'+'Obs: '+obs
            sender = 'lucas-procopio2@outlook.com'
            dest = ['lucas-procopio@outlook.com']
            mail = EmailMessage(subject, message, dest)
            mail.send()

            return render(request, 'common/succesful.html',{})
    else:
        form = QuoteForm()

    services = Service.objects.all()
    return render(request, 'common/index.html', {'services':services, 'form':form})