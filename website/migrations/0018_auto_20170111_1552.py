# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-11 13:52
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0017_auto_20170111_1539'),
    ]

    operations = [
        migrations.AddField(
            model_name='airtimedepositlead',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bankdepositlead',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='bankpaymentlead',
            name='active',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='crowdcoinpaymentlead',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]