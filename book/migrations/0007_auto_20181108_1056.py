# Generated by Django 2.1.3 on 2018-11-08 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0006_seat_chart'),
    ]

    operations = [
        migrations.AlterField(
            model_name='seat_chart',
            name='date',
            field=models.DateField(verbose_name='Date'),
        ),
    ]
