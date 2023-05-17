# Generated by Django 4.1 on 2023-04-14 17:23

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True, verbose_name='')),
                ('email', models.CharField(max_length=50, null=True, verbose_name='')),
                ('user', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_ordered', models.DateField(auto_now_add=True)),
                ('complete', models.BooleanField(blank=True, default=True, null=True)),
                ('transaction_id', models.CharField(max_length=50, null=True, verbose_name='')),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.customer', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=50, verbose_name='')),
                ('product_model', models.IntegerField(verbose_name='')),
                ('package_type', models.CharField(max_length=50, verbose_name='')),
                ('net_weight', models.CharField(max_length=50, verbose_name='')),
                ('unit_per_box', models.CharField(max_length=50, verbose_name='')),
                ('gross_weight', models.CharField(max_length=50, verbose_name='')),
                ('dimendions', models.CharField(max_length=50, verbose_name='')),
                ('bracode_number', models.IntegerField(verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='ShippingAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='')),
                ('city', models.CharField(max_length=50, null=True, verbose_name='')),
                ('state', models.CharField(max_length=50, null=True, verbose_name='')),
                ('zipcode', models.CharField(max_length=50, null=True, verbose_name='')),
                ('date_added', models.DateField(auto_now_add=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.customer', verbose_name='')),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order', verbose_name='')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('date_added', models.DateField(auto_now_add=True)),
                ('order', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.order', verbose_name='')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.product', verbose_name='')),
            ],
        ),
    ]