# Generated by Django 2.1.7 on 2019-05-04 23:19

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0050_auto_20190504_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 23, 19, 43, 136398, tzinfo=utc)),
        ),
    ]
