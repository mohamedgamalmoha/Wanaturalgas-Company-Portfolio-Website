# Generated by Django 3.1.7 on 2021-03-22 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receives', '0007_auto_20210322_1926'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mainrequests',
            name='q1',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=3, verbose_name='Is your heating and air conditioning system operating & maintaining a comfortable temperature?'),
        ),
    ]
