# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-16 08:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='courier',
            old_name='user_id',
            new_name='user_back_id',
        ),
    ]