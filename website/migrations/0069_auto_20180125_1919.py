# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-25 17:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0068_auto_20180125_1851'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pocket',
            name='voucher_receiving_fee',
            field=models.CharField(blank=True, default=b'15%', max_length=100),
        ),
        migrations.AlterField(
            model_name='pocket',
            name='voucher_sending_fee',
            field=models.CharField(blank=True, default=b'0%', max_length=100),
        ),
    ]
