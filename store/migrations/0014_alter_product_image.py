# Generated by Django 4.1 on 2023-05-11 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0013_rename_product_model_product_product_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
