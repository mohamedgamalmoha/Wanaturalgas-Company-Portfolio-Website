# Generated by Django 3.1.7 on 2021-03-21 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receives', '0004_auto_20210318_1700'),
    ]

    operations = [
        migrations.AddField(
            model_name='mainrequests',
            name='address_line',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='mainrequests',
            name='wa',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='mainrequests',
            name='city',
            field=models.CharField(max_length=250),
        ),
    ]
