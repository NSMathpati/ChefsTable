# Generated by Django 4.1.2 on 2022-11-21 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ChefsTableAPI', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='menu',
            name='menu_item_description',
            field=models.TextField(default='', max_length=1000),
        ),
    ]