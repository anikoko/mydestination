# Generated by Django 3.2.4 on 2021-06-26 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_venue_place'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='manager',
            field=models.CharField(blank=True, max_length=120),
        ),
    ]
