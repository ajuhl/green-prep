# Generated by Django 2.1.7 on 2019-04-22 02:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0037_auto_20190421_0930'),
    ]

    operations = [
        migrations.AddField(
            model_name='plan',
            name='name',
            field=models.CharField(default='default', max_length=120),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 2, 34, 55, 64173, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='savedmeal',
            name='creation_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 4, 22, 2, 34, 55, 64173, tzinfo=utc)),
        ),
    ]