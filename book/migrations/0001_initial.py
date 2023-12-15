# Generated by Django 2.1.3 on 2018-11-03 21:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('arrival', models.CharField(max_length=8, null=True, verbose_name='Arrival')),
                ('day', models.IntegerField(null=True, verbose_name='Day')),
                ('id', models.IntegerField(primary_key=True, serialize=False, verbose_name='id')),
                ('departure', models.CharField(max_length=8, null=True, verbose_name='Arrival')),
            ],
        ),
        migrations.CreateModel(
            name='Station',
            fields=[
                ('state', models.CharField(max_length=20, null=True, verbose_name='State')),
                ('code', models.CharField(max_length=10, primary_key=True, serialize=False, verbose_name='Code')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('zone', models.CharField(max_length=10, verbose_name='Zone')),
                ('address', models.CharField(max_length=50, null=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Train',
            fields=[
                ('arrival', models.CharField(max_length=8, null=True, verbose_name='Arrival')),
                ('name', models.CharField(max_length=30, verbose_name='Name')),
                ('zone', models.CharField(max_length=10, verbose_name='Zone')),
                ('number', models.IntegerField(primary_key=True, serialize=False, verbose_name='Number')),
                ('departure', models.CharField(max_length=8, null=True, verbose_name='Departure')),
                ('return_train', models.IntegerField(verbose_name='Number')),
                ('duration_h', models.IntegerField(null=True, verbose_name='Duration Hours')),
                ('duration_m', models.IntegerField(null=True, verbose_name='Duration Minutes')),
                ('type', models.CharField(max_length=5, verbose_name='Type')),
                ('distance', models.IntegerField(verbose_name='Distance')),
                ('dest', models.ForeignKey(on_delete=models.SET(None), related_name='train_dest', to='book.Station')),
                ('source', models.ForeignKey(on_delete=models.SET(None), related_name='train_source', to='book.Station')),
            ],
        ),
        migrations.AddField(
            model_name='schedule',
            name='station',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='station_schedule', to='book.Station'),
        ),
        migrations.AddField(
            model_name='schedule',
            name='train',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='train_schedule', to='book.Train'),
        ),
    ]
