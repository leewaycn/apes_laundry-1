# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-15 05:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0004_order_target_station'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='target_station',
            new_name='target_station_id',
        ),
    ]