# Generated by Django 4.1.7 on 2023-03-30 13:25

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_cuisine_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='time',
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AddField(
            model_name='reservation',
            name='reservation_slot',
            field=models.SmallIntegerField(default=10),
        ),
    ]