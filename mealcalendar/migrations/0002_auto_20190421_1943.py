# Generated by Django 2.1.7 on 2019-04-22 02:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mealcalendar', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='description',
        ),
        migrations.RemoveField(
            model_name='event',
            name='end_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='start_time',
        ),
        migrations.RemoveField(
            model_name='event',
            name='title',
        ),
    ]