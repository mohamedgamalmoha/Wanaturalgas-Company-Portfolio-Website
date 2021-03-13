from django import forms
from .models import Contact, MainRequests


class ContactForm(forms.Form):
    class Meta:
        model = Contact


class MainRequestsForm(forms.Form):
    class Meta:
        model = MainRequests
