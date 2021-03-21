from django import forms
from .models import Contact  # ,MainRequests

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget

# class MainRequestsForm(forms.ModelForm):

#     class Meta:
#         model = MainRequests
#         fields = '__all__'


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={
                'class': 'main-input', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={
                'class': 'main-input', 'placeholder': 'Last Name'}),
            'emil_address': forms.EmailInput(attrs={
                'class': 'main-input', 'placeholder': 'Email Address'}),
            'zip_code': forms.NumberInput(attrs={
                'class': 'main-input', 'placeholder': 'Zip Code'}),
            'Question': forms.Textarea(attrs={
                'class': 'main-input', 'cols': '30', 'rows': '10',
                'placeholder': ' Your Question Here'}),
            'phone_number': PhoneNumberInternationalFallbackWidget(attrs={
                'class': 'main-input', 'placeholder': 'Phone Number'}),
        }
