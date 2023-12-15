# Generated by Django 2.1.3 on 2018-11-08 10:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0005_auto_20181108_0929'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seat_Chart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_ac', models.IntegerField(verbose_name='1st AC')),
                ('second_ac', models.IntegerField(verbose_name='2nd AC')),
                ('third_ac', models.IntegerField(verbose_name='3rd AC')),
                ('sleeper', models.IntegerField(verbose_name='Sleeper')),
                ('date', models.DateTimeField(verbose_name='Date')),
                ('train', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train_chart', to='book.Train')),
            ],
        ),
    ]
