# Generated by Django 4.1.6 on 2023-03-16 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inputf',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('time_log', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250, verbose_name='Name')),
                ('contact', models.CharField(max_length=200, verbose_name='Phone Number')),
                ('time', models.TimeField(auto_now=True)),
                ('count', models.IntegerField()),
                ('notes', models.CharField(max_length=650, verbose_name='Note')),
            ],
        ),
    ]