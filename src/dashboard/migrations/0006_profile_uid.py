# Generated by Django 2.2.1 on 2019-06-12 10:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0005_auto_20190612_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='uid',
            field=models.CharField(blank=True, editable=False, max_length=30, null=True),
        ),
    ]
