# Generated by Django 2.2.1 on 2019-06-18 10:26

from django.db import migrations, models
import products.models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0026_auto_20190618_1126'),
    ]

    operations = [
        migrations.AddField(
            model_name='productimage',
            name='height',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='productimage',
            name='media',
            field=models.ImageField(blank=True, height_field='height', null=True, upload_to=products.models.media_location, validators=[products.models.image_validation], width_field='width'),
        ),
        migrations.AddField(
            model_name='productimage',
            name='width',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]