# Generated by Django 3.2.4 on 2021-06-26 20:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_alter_event_manager'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='venue',
            name='place',
        ),
        migrations.AlterField(
            model_name='venue',
            name='name',
            field=models.CharField(max_length=300, verbose_name='Venue Name'),
        ),
    ]
