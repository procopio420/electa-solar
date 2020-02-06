# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Application
from common.forms import QuoteForm

# Create your views here.
def apps(request):
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
            dest = 'lucas-procopio@outlook.com'
            send_mail(subject,message,sender,dest)

            return render(request, 'common/succesful.html',{'form':form})
    else:
        form = QuoteForm()

    apps = Application.objects.all()
    return render(request, 'apps/apps.html', {'apps':apps, 'form':form})