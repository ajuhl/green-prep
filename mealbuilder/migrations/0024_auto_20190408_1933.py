# Generated by Django 2.1.7 on 2019-04-08 19:33

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0023_auto_20190407_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 8, 19, 33, 46, 704458, tzinfo=utc)),
        ),
    ]
