from django import forms

class QuoteForm(forms.Form):
    name = forms.CharField(label='First Name: ', max_length=150)
    lname = forms.CharField(label='Last Name: ', max_length=150)
    phone = forms.CharField(label='Phone number: ', max_length=25)
    email = forms.EmailField(label='Email: ')
    address = forms.CharField(label='Address: ', max_length=250)
    obs = forms.CharField(label='Observations: ', max_length=150, required=False, widget=forms.Textarea)