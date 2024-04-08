# Generated by Django 4.2 on 2024-03-26 14:53

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('category', models.CharField(max_length=100)),
                ('general_ledger_code', models.IntegerField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PettyCash',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_date', models.DateField(default=datetime.datetime(2024, 3, 26, 14, 53, 33, 147435, tzinfo=datetime.timezone.utc))),
                ('cash_flow', models.CharField(choices=[('Cash In', 'Cash In'), ('Cash Out', 'Cash Out')], max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('description', models.CharField(max_length=1200)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pettycash_app.category')),
            ],
        ),
    ]