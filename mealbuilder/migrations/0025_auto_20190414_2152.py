# Generated by Django 2.1.7 on 2019-04-14 21:52

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0024_auto_20190414_2139'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 14, 21, 52, 34, 979336, tzinfo=utc)),
        ),
    ]