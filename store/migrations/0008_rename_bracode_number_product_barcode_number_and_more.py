# Generated by Django 4.1 on 2023-04-19 04:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_brand_name_product_brand_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='bracode_number',
            new_name='barcode_number',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='dimendions',
            new_name='dimensions',
        ),
    ]
