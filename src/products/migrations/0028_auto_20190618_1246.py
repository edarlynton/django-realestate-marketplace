# Generated by Django 2.2.1 on 2019-06-18 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20190618_1126'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='pid',
            field=models.IntegerField(blank=True, editable=False, max_length=30, null=True, unique=True),
        ),
    ]
