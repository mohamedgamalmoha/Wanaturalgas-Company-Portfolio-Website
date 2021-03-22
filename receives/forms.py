from django import forms
from .models import Contact, MainRequests

from phonenumber_field.widgets import PhoneNumberInternationalFallbackWidget


class MainRequestsForm(forms.ModelForm):
    #
    # def __int__(self, *args, **kwargs):
    #
    #     ages = (
    #         ('0 - 5 years', '0 - 5 years'),
    #         ('6 - 10 years', '6 - 10 years'),
    #         ('11 - 15 years', '11 - 15 years'),
    #         ('16 - 20 years', '16 - 20 years'),
    #     )
    #     self.fields['equipment_age'].queryset = ages
    #     super(MainRequestsForm, self).__init__(*args, **kwargs)

    class Meta:
        model = MainRequests
        fields = '__all__'
        widgets = {
            'equipment_age': forms.RadioSelect(),
        }


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
