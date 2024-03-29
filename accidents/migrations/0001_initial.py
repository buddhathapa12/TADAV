# Generated by Django 2.2.2 on 2019-06-13 14:29

import datetime
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Accident',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('latitude', models.DecimalField(decimal_places=6, max_digits=10)),
                ('accident_catagory', models.CharField(max_length=100)),
                ('municipality', models.CharField(max_length=100)),
                ('urban_or_not', models.BooleanField()),
                ('scene_description', models.CharField(max_length=100)),
                ('cause_of_accident', models.CharField(max_length=100)),
                ('accident_type', models.CharField(max_length=100)),
                ('traffic_condition', models.CharField(max_length=100)),
                ('date', models.DateField(default=datetime.date.today)),
                ('day_of_week', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(7)])),
                ('time', models.DateTimeField()),
                ('road_type', models.CharField(max_length=100)),
                ('weather_condition', models.CharField(max_length=100)),
                ('road_surface_condition', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Municipality',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('municipality_name', models.CharField(max_length=100)),
                ('no_of_inhabitants', models.IntegerField()),
                ('area_size', models.DecimalField(decimal_places=10, max_digits=20)),
            ],
        ),
        migrations.CreateModel(
            name='Victim',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('caused_the_accident', models.BooleanField()),
                ('age', models.IntegerField()),
                ('sex', models.BooleanField(null=True)),
                ('municipality', models.CharField(max_length=100)),
                ('citizenship', models.CharField(max_length=100)),
                ('injury', models.CharField(max_length=100)),
                ('type_of_person', models.CharField(max_length=100)),
                ('safety_belt_or_helmet', models.BooleanField()),
                ('years_of_driving', models.IntegerField()),
                ('age_discrete', models.IntegerField()),
            ],
        ),
    ]
