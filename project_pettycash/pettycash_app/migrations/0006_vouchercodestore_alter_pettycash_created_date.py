# Generated by Django 4.2 on 2024-03-27 10:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pettycash_app', '0005_pettycash_to_or_from_alter_pettycash_created_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='VoucherCodeStore',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('voucher_code', models.CharField(max_length=200)),
            ],
        ),
        migrations.AlterField(
            model_name='pettycash',
            name='created_date',
            field=models.DateField(default=datetime.datetime(2024, 3, 27, 10, 38, 37, 313105, tzinfo=datetime.timezone.utc)),
        ),
    ]
