# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Building',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=300)),
                ('location_description', models.TextField(blank=True)),
                ('building_apartments', models.IntegerField(blank=True, null=True)),
                ('picture', models.ImageField(blank=True, null=True, upload_to='building/')),
            ],
            options={
                'ordering': ('adress',),
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress', models.CharField(max_length=300)),
                ('number_of_apartment', models.IntegerField(blank=True, null=True)),
                ('type_department', models.CharField(max_length=50, verbose_name='Type')),
                ('bedrooms', models.IntegerField(blank=True, null=True)),
                ('bathrooms', models.IntegerField(blank=True, null=True)),
                ('rent', models.FloatField(blank=True, help_text='Amount of money per month', null=True)),
                ('deposit', models.FloatField(blank=True, help_text='Amount of money $$$ for deposit', null=True)),
                ('parking', models.CharField(blank=True, max_length=100)),
                ('pets', models.CharField(blank=True, max_length=50)),
                ('utilities', models.CharField(blank=True, max_length=200)),
                ('kitchen', models.CharField(blank=True, max_length=200)),
                ('laundry', models.CharField(blank=True, max_length=100)),
                ('lease_term', models.CharField(blank=True, max_length=50)),
                ('unit_description', models.TextField()),
                ('building', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='buildings.Building')),
            ],
            options={
                'ordering': ('adress',),
            },
        ),
        migrations.CreateModel(
            name='NearbyAtraction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo_img', models.CharField(max_length=100)),
                ('building', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='buildings.Building')),
            ],
        ),
    ]
