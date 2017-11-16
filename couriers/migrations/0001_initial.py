# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-14 09:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Courier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('idcard_url', models.CharField(max_length=20)),
                ('health_url', models.CharField(max_length=20)),
                ('workplace', models.CharField(max_length=50)),
                ('is_locked', models.BooleanField()),
                ('is_checked', models.BooleanField()),
                ('create_at', models.DateField()),
                ('update_at', models.DateField()),
                ('user_id', models.IntegerField()),
            ],
            options={
                'db_table': 'couriers',
            },
        ),
    ]