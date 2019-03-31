# Generated by Django 2.1.7 on 2019-03-31 01:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0016_auto_20190331_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 31, 1, 28, 7, 978237, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='quantity',
            field=models.DecimalField(decimal_places=2, max_digits=6, null=True),
        ),
    ]
