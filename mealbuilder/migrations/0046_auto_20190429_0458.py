# Generated by Django 2.1.7 on 2019-04-29 04:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0045_auto_20190422_1801'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 29, 4, 58, 30, 271390, tzinfo=utc)),
        ),
    ]
