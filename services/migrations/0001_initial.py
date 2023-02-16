# Generated by Django 3.2 on 2023-02-14 21:53

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('service_type', models.CharField(choices=[('GEL', 'Gel'), ('SHELLAC', 'Shellac'), ('BROWS', 'Brows'), ('HENNA', 'Henna')], max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5, validators=[django.core.validators.MinValueValidator(Decimal('15.00')), django.core.validators.MaxValueValidator(Decimal('300.00'))])),
            ],
        ),
    ]
