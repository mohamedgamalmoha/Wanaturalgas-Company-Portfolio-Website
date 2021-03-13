from django.db import models

from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField


class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    emil_address = models.EmailField()
    phone_number = PhoneNumberField(null=True)
    zip_code = models.PositiveIntegerField()
    Question = models.TextField()

    class Meta:
        verbose_name = 'Contact Us Message'
        verbose_name_plural = 'Contact Us Messages'

    def __str__(self):
        return f"Message from: {self.first_name}"


class MainRequests(models.Model):
    q1 = models.BooleanField(
        'Is your heating and air conditioning system operating & maintaining a comfortable temperature?',
    )
    home_temperature = models.IntegerField('What is the temperature of your home?')
    interest_fields = (
        ('Repair', 'Repair'),
        ('Maintenance', 'Maintenance'),
        ('Replacement / New install of equipment', 'Replacement / New install of equipment'),
        ('Other', 'Other'),
        )
    field_of_interest = MultiSelectField('Are you interested in?',
                                         choices=interest_fields)
    issues = (
        ('Furnace', 'Furnace'),
        ('Air Conditioner', 'Air Conditioner'),
        ('Heat Pump-Ducted', 'Heat Pump-Ducted'),
        ('Heat Pump-Ductless Mini Split', 'Heat Pump-Ductless Mini Split'),
        ('Water Heater-Tank', 'Water Heater-Tank'),
        ('Water Heater-Tankless', 'Water Heater-Tankless'),
        ('Electronic Air Cleaner (EAC)', 'Electronic Air Cleaner (EAC)'),
        ('Gas Fireplace', 'Gas Fireplace'),
        ('Gas Piping', 'Gas Piping'),
    )
    issue_of_concern = MultiSelectField('Regarding what type of equipment or issue of concern:', choices=issues)
    ages = (
        ('0 - 5 years', '0 - 5 years'),
        ('6 - 10 years', '6 - 10 years'),
        ('11 - 15 years', '11 - 15 years'),
        ('16 - 20 years', '16 - 20 years'),
    )
    equipment_age = models.CharField('Approximate age of equipment',
                                     choices=ages, max_length=50)

    first_name = models.CharField(max_length=250)
    second_name = models.CharField(max_length=250)
    emil_address = models.EmailField()
    contact_number = PhoneNumberField()
    cell_number = PhoneNumberField()

    address = models.CharField(max_length=150)
    city = models.CharField(max_length=50)
    zip_code = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Received Request'
        verbose_name_plural = 'Received Requests'

    def __str__(self):  # Will create request ID later
        return "Request"
