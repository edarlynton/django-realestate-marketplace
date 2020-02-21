# Generated by Django 2.2.1 on 2019-06-13 10:32

import dashboard.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_profile_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(blank=True, height_field='height_field', null=True, upload_to=dashboard.models.image_upload_to_profile, validators=[dashboard.models.image_validation], width_field='width_field'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uid',
            field=models.CharField(blank=True, editable=False, max_length=30, null=True, unique=True),
        ),
    ]