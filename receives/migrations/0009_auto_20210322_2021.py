# Generated by Django 3.1.7 on 2021-03-22 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('receives', '0008_auto_20210322_1935'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mainrequests',
            old_name='emil',
            new_name='email',
        ),
    ]
