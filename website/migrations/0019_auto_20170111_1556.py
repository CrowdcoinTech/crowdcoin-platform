# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-01-11 13:56
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0018_auto_20170111_1552'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='airtimedepositlead',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='bankdepositlead',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='bankpaymentlead',
            name='updated',
        ),
        migrations.RemoveField(
            model_name='crowdcoinpaymentlead',
            name='updated',
        ),
    ]