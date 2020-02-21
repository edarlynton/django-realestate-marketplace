# Generated by Django 2.2.1 on 2019-06-15 09:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0009_auto_20190614_2250'),
    ]

    operations = [
        migrations.RenameField(
            model_name='clientrequest',
            old_name='number_of_bedroom',
            new_name='bedroom',
        ),
        migrations.RemoveField(
            model_name='clientrequest',
            name='phone_number',
        ),
        migrations.AddField(
            model_name='clientrequest',
            name='phone',
            field=models.CharField(default=2, max_length=11, validators=[django.core.validators.RegexValidator(code='invalid number', message='Please enter a valid phone number', regex='^[0-9]{11}$')]),
            preserve_default=False,
        ),
    ]