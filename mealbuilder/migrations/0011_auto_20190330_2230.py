# Generated by Django 2.1.7 on 2019-03-30 22:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0010_auto_20190330_1915'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 30, 22, 30, 57, 260133, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='mealitem',
            name='food_portion',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True),
        ),
    ]