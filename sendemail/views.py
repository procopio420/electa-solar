from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from .forms import QuoteForm

def emailView(request):
    if request.method == 'GET':
        form = QuoteForm()
    else:
        form = QuoteForm(request.POST)
        if form.is_valid():
            subject = 'Quote request!'
            from_email = 'quotes@electasolar.com'
            name = form.cleaned_data['name']
            lname = form.cleaned_data['lname']
            phone = form.cleaned_data['phone']
            email = form.cleaned_data['email']
            address = form.cleaned_data['address']
            obs = form.cleaned_data['obs']
            
            message = 'Name: '+name+' '+lname+'\n'+'Phone: '+phone+'\n'+'Email: '+email+'\n'+'Address: '+address+'\n'+'Obs: '+obs
            try:
                send_mail(subject, message, from_email, ['electasolar@gmail.com', 'lucas-procopio2@outlook.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, "sendemail/email.html", {'form': form})

def successView(request):
    return render(request, 'sendemail/success.html', {})