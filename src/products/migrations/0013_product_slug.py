# Generated by Django 2.2.1 on 2019-06-13 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_remove_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(blank=True, null=True),
        ),
    ]