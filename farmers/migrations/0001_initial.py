# Generated by Django 5.1.2 on 2024-11-09 11:16

import django.db.models.deletion
import django.utils.crypto
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Farmer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('farmer_id', models.CharField(default=django.utils.crypto.get_random_string, editable=False, max_length=10, unique=True)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(max_length=10)),
                ('age', models.IntegerField()),
                ('land_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('county', models.CharField(max_length=100)),
                ('subcounty', models.CharField(max_length=100)),
                ('parish', models.CharField(max_length=100)),
                ('village', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Harvest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=20)),
                ('land_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potato_kg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('date_reported', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='PlantingReport',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('season', models.CharField(max_length=20)),
                ('land_size', models.DecimalField(decimal_places=2, max_digits=5)),
                ('potato_kg', models.DecimalField(decimal_places=2, max_digits=5)),
                ('planting_date', models.DateField()),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmer')),
            ],
        ),
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('issue', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('farmer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='farmers.farmer')),
            ],
        ),
    ]
