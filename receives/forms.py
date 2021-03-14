from django import forms
from .models import Contact, MainRequests


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'


class MainRequestsForm(forms.ModelForm):
    class Meta:
        model = MainRequests
        fields = '__all__'
