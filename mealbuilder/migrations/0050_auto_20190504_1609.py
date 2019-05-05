# Generated by Django 2.1.7 on 2019-05-04 23:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mealbuilder', '0049_auto_20190503_2148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='food',
            name='cholesterol',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='magnesium',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='potassium',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='sat_fat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='sodium',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='sugars',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='total_fat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='food',
            name='trans_fat',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='calories',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='carbs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='cholesterol',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='create_date',
            field=models.DateTimeField(default=datetime.datetime(2019, 5, 4, 23, 9, 47, 643039, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='meal',
            name='fiber',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='magnesium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='potassium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='protein',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='sat_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='sodium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='sugars',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='total_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='meal',
            name='trans_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='carbs',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='cholesterol',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='fiber',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='magnesium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='potassium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='protein',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sat_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sodium',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='sugars',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='total_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='plan',
            name='trans_fat',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
