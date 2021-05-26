# Generated by Django 3.2.3 on 2021-05-26 12:33

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bid', '0013_alter_bid_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='bid_amount',
            field=models.DecimalField(decimal_places=2, max_digits=9),
        ),
        migrations.AlterField(
            model_name='bid',
            name='created_at',
            field=models.DateTimeField(auto_created=True, default=datetime.datetime(2021, 5, 26, 18, 33, 22, 405342)),
        ),
    ]