# Generated by Django 4.1.5 on 2023-02-05 22:49

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_bookingmodel_allergies'),
    ]

    operations = [
        migrations.AlterField(
            model_name='createreviews',
            name='creation_date',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
