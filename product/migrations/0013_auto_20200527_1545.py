# Generated by Django 3.0.6 on 2020-05-27 12:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0012_product_prdimage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='PROBrand',
            new_name='PRDBrand',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='PROCategory',
            new_name='PRDCategory',
        ),
    ]
