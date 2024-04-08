# Generated by Django 4.2 on 2024-03-27 14:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash_app', '0011_alter_pettycash_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openingbalance',
            name='opening_balance',
            field=models.DecimalField(decimal_places=2, max_digits=50),
        ),
        migrations.AlterField(
            model_name='pettycash',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 27, 14, 10, 2, 848789, tzinfo=datetime.timezone.utc)),
        ),
    ]