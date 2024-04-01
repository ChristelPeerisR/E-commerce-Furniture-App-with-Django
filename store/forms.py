# forms.py
from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter your Name'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder':'Enter your Email'}))
    subject = forms.CharField(label='Suject', max_length=50, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Enter Subject'}))
    phone_no = forms.IntegerField(label='Phone no' , widget=forms.NumberInput(attrs={'class': 'form-control', 'placeholder':'Enter your Phone Number'}))
    message = forms.CharField(label='Message', widget=forms.Textarea(attrs={'class': 'form', 'placeholder':'Enter your message in detail..'}))
