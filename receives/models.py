from django.db import models
from django.db.models.signals import pre_save
from multiselectfield import MultiSelectField
from phonenumber_field.modelfields import PhoneNumberField

from wanaturalgas.utils import unique_request_id_generator


CHOICES = (
    ('Yes', 'Yes'),
    ('No', 'No')
)


class Contact(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250, blank=True, null=True)
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
    request_id = models.CharField(max_length=120, blank=True)
    q1 = models.CharField(
        'Is your heating and air conditioning system operating & maintaining a comfortable temperature?',
        choices=CHOICES, max_length=3
    )
    home_temperature = models.CharField('What is the temperature of your home?', max_length=255)
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
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    contact_phone = PhoneNumberField()
    cell_phone = PhoneNumberField()

    street_address = models.CharField(max_length=150)
    address_line_2 = models.CharField(max_length=250, null=True, blank=True)
    wa = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250)
    zip_code = models.PositiveIntegerField()

    class Meta:
        verbose_name = 'Received Request'
        verbose_name_plural = 'Received Requests'

    def __str__(self):
        return f"Request No. {self.request_id}"


def pre_save_request_id(sender, instance, *args, **kwargs):
    if not instance.request_id:
        instance.request_id = unique_request_id_generator(instance)


pre_save.connect(pre_save_request_id, sender=MainRequests)
