# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-12-16 01:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_order_customer_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='user_id',
            new_name='customer_id',
        ),
    ]
